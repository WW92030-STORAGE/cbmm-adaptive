with open("outputLoad.txt", "r") as FILE:
    for line in FILE:
        # line no commas
        LNC = ""
        for c in line:
            if c != ',':
                LNC += c

        LNC = LNC.strip()
            
        if "Throughput" in LNC:
            print(LNC)
        if "AverageLatency" in LNC:
            print(LNC)
        if "99thPercentile" in LNC:
            print(LNC)
# Needed prints

print("RELEVANT DATA")

with open("outputLoad.txt", "r") as FILE:
    for line in FILE:
        # line no commas
        LNC = ""
        for c in line:
            if c != ',':
                LNC += c

        LNC = LNC.strip()
        sp = LNC.split()

        if "CLEANUP" in LNC:
            continue
            
        if "Throughput" in LNC:
            print(sp[2])
        if "AverageLatency" in LNC:
            print(sp[2])
with open("outputLoad.txt", "r") as FILE:
    for line in FILE:
        LNC = ""
        for c in line:
            if c != ',':
                LNC += c

        LNC = LNC.strip()
        sp = LNC.split()
        if "CLEANUP" in LNC:
            continue
        if "99thPercentile" in LNC:
            print(sp[2])

