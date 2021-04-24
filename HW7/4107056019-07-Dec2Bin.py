import struct
def dec2bin(n):
    n = struct.unpack('I', struct.pack('f', n))[0]
    return "{:032b}".format(n)

print("1. Reading sideinfodeci.txt", end = '\t')
buffer = ''
try:
    with open("sideinfodeci.txt", "r") as f:
        line = f.readline()
        while line:
            buffer += "{:s}\n".format(dec2bin(float(line.strip("\n"))))
            line = f.readline()
    print("✅")
except ValueError:
    print("❌")
    print("sideinfodeci.txt has non floating string")
    exit()
except FileNotFoundError:
    print("❌")
    print("File sideinfodeci.txt not found")
    exit()
except:
    print("❌")
    exit()

print("2. Writing sideinfobina.txt", end = '\t')
try:
    with open("sideinfobina.txt", "w") as f:
        f.write(buffer)
    print("✅")
except:
    print("❌")
    exit()
