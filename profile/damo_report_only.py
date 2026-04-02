import time, datetime, math
from bisect import bisect_right, bisect_left
import subprocess

BUCKET_ORDER = 8                   # Log of how many buckets there are (ONLY CHANGE THIS)
BUCKET_SHIFT = 48 - BUCKET_ORDER    # Log of how big each bucket is
NUM_BUCKETS = 1 << BUCKET_ORDER  
BUCKET_SIZE = 1 << BUCKET_SHIFT   # how big the bucket is, in terms of powers of 2 of the bucket size

DEBUG = False

def exec_(cmd):
    return subprocess.run(cmd, shell = True,     
    capture_output=True,
    text=True,
    check=True # Optional: raise an exception if the command fails
    ).stdout

def compute_approximate_interactions(start, end, S, E, A):
    length = end - start
    if length <= 0:
        return 0

    total = 0

    # start from any potential overlaps
    i = bisect_left(E, start)

    while i < len(S) and S[i] < end:
        overlap = min(end, E[i]) - max(start, S[i])
        if overlap > 0:
            total += A[i] * overlap
        i += 1

    return total / length

    
def SET_STARTS(bucket, val):
    with open("/proc/set_starts", 'w') as FILE:
        FILE.write(str(bucket) + " " + str(val))

def SET_ENDS(bucket, val):
    with open("/proc/set_ends", 'w') as FILE:
        FILE.write(str(bucket) + " " + str(val))

def SET_BENEFITS(bucket, val):
    with open("/proc/set_benefits", 'w') as FILE:
        FILE.write(str(bucket) + " " + str(val))

def INCREASE_BENEFITS(bucket, val):
    with open("/proc/increase_benefits", 'w') as FILE:
        val2 = abs(val)
        thing = 1 if val >= 0 else 0
        FILE.write(str(bucket) + " " + str(val2) + " " + str(thing))

def SCALE_BENEFITS(bucket, n, d):
    with open("/proc/scale_benefits", 'w') as FILE:
        FILE.write(str(bucket) + " " + str(n) + " " + str(d))


APPROX_TO_BUCKETS = False
MODE = "multiplicative2"

DO_NOTHING = False
NO_UPDATES = False

def main(records, cmd_fields):
    if DO_NOTHING:
        return
    STARTS = []
    ENDS = []
    ACCESSES = []

    with open("damo_report.txt", "r") as FILE:
        for line in FILE:
            line_s = line.split()
            STARTS.append(int(line_s[0]))
            ENDS.append(int(line_s[1]))
            ACCESSES.append(int(line_s[2]))

    # print(datetime.datetime.now())
    # print(records)
    # print(cmd_fields)
    if DEBUG:
        print("BEGIN RECORDS")

        print("S", STARTS)
        print("E", ENDS)
        print("A", ACCESSES)

    if len(STARTS) == 0:
        N = 0
        with open("damo_report.txt", 'w') as FILE:
            for rec in records:
                for s in rec.snapshots:
                    for r in s.regions:
                        info = str(r.start) + " " + str(r.end) + " " + str(r.nr_accesses.samples)
                        FILE.writelines(info + "\n")
                        N += 1
                break
        if not NO_UPDATES:
            with open("/proc/set_prof_size", "w") as PROC:
                PROC.write(str(N))

            i = 0
            for rec in records:
                for s in rec.snapshots:
                    for r in s.regions:
                        SET_STARTS(i, r.start)
                        SET_ENDS(i, r.end)
                        i += 1
                break

        return

    N = 0
    for rec in records:
        for s in rec.snapshots:
            for r in s.regions:
                N += 1

        break
    
    print("N", N, len(STARTS))


    if (not APPROX_TO_BUCKETS) and (N != len(STARTS)):
        # exec_("echo \"%d\" | sudo tee /proc/set_prof_size" % (N))
        if not NO_UPDATES:
            with open("/proc/set_prof_size", "w") as PROC:
                PROC.write(str(N))
            
            # populate with default values if sucky
            if N > len(STARTS):
                for i in range(len(STARTS), N):
                    # CHANGE THE DEFAULT VALUE HERE
                    SET_BENEFITS(i, 200000)       # 21531397

    with open("damo_report.txt", 'w') as FILE:
        i = 0
        if DEBUG:
            print("PERIOD " + str(datetime.datetime.now()) + "\n")
        for rec in records:
            if DEBUG:
                print("RECORD\n")
            for s in rec.snapshots:
                for r in s.regions:
                    info = str(r.start) + " " + str(r.end) + " " + str(r.nr_accesses.samples)
                    FILE.writelines(info + "\n")

                    if DEBUG:
                        print("INTERVAL", info)
                    approx_access = compute_approximate_interactions(r.start, r.end, STARTS, ENDS, ACCESSES)
                    if DEBUG:
                        print("PRIOR_APPROX_ACCESS", approx_access)

                    if (not NO_UPDATES) and (approx_access > 0 and r.nr_accesses.samples > 0):
                        if APPROX_TO_BUCKETS:
                            ii = (r.start - 1) >> BUCKET_SHIFT if r.start > 0 else 0
                            while ii < (NUM_BUCKETS) and (ii << BUCKET_SHIFT) < r.end:
                                print(r.start, r.end, ii, (ii << BUCKET_SHIFT), ((ii + 1) << BUCKET_SHIFT))
                                SCALE_BENEFITS(ii, r.nr_accesses, approx_access)
                                ii += 1

                            # exec_("echo \"%d\" \"%d\" \"%d\" | sudo tee /proc/scale_benefits" % (i, r.nr_accesses.samples, approx_access))
                            # SCALE_BENEFITS(i, r.nr_accesses.samples, approx_access)
                        else:
                            # set the interval and whatever
                            SET_STARTS(i, r.start)
                            SET_ENDS(i, r.end)
                            if MODE == "multiplicative":
                                SCALE_BENEFITS(i, r.nr_accesses.samples, approx_access)
                            if MODE == "multiplicative2":
                                SCALE_BENEFITS(i, 1 + r.nr_accesses.samples, approx_access)
                            elif MODE == "additive":
                                dx = r.nr_accesses.samples - approx_access
                                true_dx = math.sqrt(abs(dx)) * (1 if dx >= 0 else -1)
                                INCREASE_BENEFITS(i, int(true_dx))
                    i += 1
            break
                        
    
    
    if DEBUG:
        print("END RECORDS")

"""

10000 - 20000 ...     <- region 0 (bucket 0) in the profile (has some benefit)
20000 - 40000 ...


0 - 10000             <- region 0 (bucket 0) in the profile (and has the same benefit as the new bucket 1)
10000 - 20000         <- bucket 1 (wrong benefit)

"""

"""

maintain a shadow copy of the profile in the python program ( do a simulation)

but how does that help us?
1. damo for the most part does not have severe interval changes
2. what to do when these changes happen


"""

