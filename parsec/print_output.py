def process(encoding):
    try:
        if encoding[-1] == 's':
            encoding = encoding[:-1]
        
        if 'm' in encoding:
            xx = encoding.find('m')
            minute = encoding[:xx]
            second = encoding[xx+1:]
            return 1000 * (60 * float(minute) + float(second))
        else:
            return 1000 * float(second)
    except Exception as e:
        print("bad:", e)
    return 0


with open("output.txt", 'r') as FILE:
    for line in FILE:
        if "real" in line:
            elapsed_ms = process(line.split()[1])
            print("RUNTIME: " + str(elapsed_ms))