import time, datetime, math

BUCKET_ORDER = 10                    # Log of how many buckets there are (ONLY CHANGE THIS)
BUCKET_SHIFT = 48 - BUCKET_ORDER    # Log of how big each bucket is
NUM_BUCKETS = 1 << BUCKET_ORDER  
BUCKET_SIZE = 1 << BUCKET_SHIFT   # how big the bucket is, in terms of powers of 2 of the bucket size

FILE_PRINT = True
RAW_PRINTS = True
DEBUG = False

def smallest_bucket_index_at_least(v):
    if v < 0:
        return 0
    value = v >> BUCKET_SHIFT
    if v % (1 << BUCKET_SHIFT) != 0:
        value += 1
    return value

def largest_bucket_index_at_most(v):
    if v < 0:
        return 0
    return (v - 1) >> BUCKET_SHIFT

def main(records, cmd_fields):
    print(datetime.datetime.now())
    print(records)
    print(cmd_fields)
    print("BEGIN RECORDS")

    histogram = [0] * NUM_BUCKETS
    with open("damo_report.txt", 'a') as FILE:
        if FILE_PRINT and RAW_PRINTS:
            FILE.writelines("PERIOD " + str(datetime.datetime.now()) + "\n")
        for rec in records:
            if FILE_PRINT and RAW_PRINTS:
                FILE.writelines("RECORD\n")
            for s in rec.snapshots:
                for r in s.regions:
                    if r.nr_accesses.samples == 0 and r.nr_accesses.hz is None:
                        continue
                    if FILE_PRINT:
                        info = str(r.start) + " " + str(r.end) + " " + str(r.nr_accesses.samples)
                        if RAW_PRINTS:
                            FILE.writelines(info + "\n")

                        sbi = smallest_bucket_index_at_least(r.start)
                        ebi = largest_bucket_index_at_most(r.end) 

                        # Special case: only one bucket
                        if (sbi > ebi):
                            histogram[r.start >> BUCKET_SHIFT] += r.nr_accesses.samples
                            continue

                        """

                        The address range [r.start ... r.end) now splits into three chunks
                        [r.start, sbi<<BS)
                        [sbi<<BS, ebi<<BS) containing sbi_ebi_indexes buckets
                        [ebi<<BS, r.end)

                        The two end intervals might have zero elements.

                        """
                        sbi_ebi_indexes = (ebi - sbi)
                        second_interval = sbi_ebi_indexes << BUCKET_SHIFT

                        # bucket (sbi - 1)
                        first_interval = (sbi << BUCKET_SHIFT) - r.start
                        third_interval = r.end - (ebi << BUCKET_SHIFT)

                        total_size = r.end - r.start
                        p_first = first_interval / total_size
                        p_third = third_interval / total_size
                        p_second = second_interval / total_size

                        if DEBUG:
                            interval_info = str(sbi) + " " + str(ebi) + " | " + str(sbi << BUCKET_SHIFT) + " " + str(ebi << BUCKET_SHIFT) + "\n"
                            interval_info = interval_info + str(total_size) + " " + str(p_first) + " " + str(p_second) + " " + str(p_third)
                            FILE.writelines(interval_info)

                        if first_interval > 0 and sbi > 0:
                            histogram[sbi - 1] += p_first * r.nr_accesses.samples
                        histogram[ebi] += p_third * r.nr_accesses.samples
                        if sbi_ebi_indexes > 0:
                            weight = (p_second / sbi_ebi_indexes)
                            for i in range(sbi, ebi, 1):
                                histogram[i] += weight * r.nr_accesses.samples
        if DEBUG:
            FILE.writelines("HISTOGRAM:\n" + str([(i, histogram[i]) for i in range(len(histogram))]) + "\n")
        nonzero_histos = []
        for i in range(len(histogram)):
            if histogram[i] != 0:
                nonzero_histos.append((i, histogram[i]))
        FILE.writelines("HISTOGRAM (nonzero): " + str(nonzero_histos) + "\n")
        FILE.writelines("\n")     

        print("NONZERO_HISTOS:", nonzero_histos)  
    
    
    print("END RECORDS")

