# WARNING: Run as root

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

if __name__ == "__main__":
    SET_BENEFITS(0, 2000000)
    INCREASE_BENEFITS(0, -10000)
    SCALE_BENEFITS(0, 5, 3)