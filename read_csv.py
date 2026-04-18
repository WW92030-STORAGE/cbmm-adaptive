

CSV = "canneal"

def read_csv(csv = CSV):
    indent = "\t"
    seb = {}
    
    with open(csv + ".csv", 'r') as file:
        for line in file:
            arr = line.strip().split()
            seb[(arr[-4], arr[-1], arr[2])] = 0

    with open(csv + ".dat", 'w') as output:
        output.write("void init_values(void) {\n")
        output.write(indent + "if (HAS_INIT) return;\n")
        output.write(indent + "else HAS_INIT = true;\n")
        output.write(indent + "printk(\"INIT VALUES\\n\");\n\n")
        counter = 0

        for entry in seb:
            arr = line.strip().split()
            output.write(indent + "STARTS[" + str(counter) + "] = " + str(entry[0]) + ";\n")
            output.write(indent + "ENDS[" + str(counter) + "] = " + str(entry[1]) + ";\n")
            output.write(indent + "BENEFITS[" + str(counter) + "] = " + str(entry[2]) + ";\n")

            counter += 1

        output.write(indent + "PROFILE_SIZE = " + str(counter) + ";\n")
        output.write("}\n")

    with open(csv + "_py.dat", 'w') as output:
        output.write("\tcbmm.SET_PROF_SIZE(" + str(len(seb)) + ")\n")
        counter = 0
        for entry in seb:
            arr = line.strip().split()
            output.write("\tcbmm.SET_STARTS(" + str(counter) + ", " + str(entry[0]) + ")\n")
            output.write("\tcbmm.SET_ENDS(" + str(counter) + ", " + str(entry[1]) + ")\n")
            output.write("\tcbmm.SET_BENEFITS(" + str(counter) + ", " + str(entry[2]) + ")\n")

            counter += 1

    with open(csv + "_py_list.dat", 'w') as output:
        output.write("\tPOLICY = []\n")
        for entry in seb:
            arr = line.strip().split()
            output.write("\tPOLICY.append((" + str(entry[0]) + ", " + str(entry[1]) + ", " + str(entry[2]) + "))\n")



if __name__ == "__main__":
    read_csv()

