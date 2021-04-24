class Need32Char(Exception):
    def __init__(self):
        super().__init__("bin2dec() argument[0]'s length should be 32")

def bin2dec(string32):
    if len(string32) != 32:
        raise Need32Char
    
    sign     = int(string32[0])
    exponent = int(string32[1:9], 2)
    mantissa = int(string32[9:32], 2) / (2 ** 23)

    # handle denormal form
    if exponent == 0:        # 00000000
        if mantissa == 0:
            return 0
        else:
            return (mantissa) * 2 ** (exponent - 126)
    if exponent == 0xff:     # 11111111
        return '-Inf' if sign == 1 else '+Inf'

    return (1 + mantissa) * 2 ** (exponent - 127)

print("1. Reading sideinfobina.txt", end='\t')
buffer = ''
try:
    with open("sideinfobina.txt", "r") as f:
        line = f.readline()
        while line:
            buffer += "{:.4f}\n".format(bin2dec(line.strip("\n")))
            line = f.readline()
    print("✅")
except Need32Char:
    print("❌")
    print("bin2dec() argument[0]'s length should be 32")
    exit()
except FileNotFoundError:
    print("❌")
    print("File sideinfobina.txt not found")
    exit()
except ValueError:
    print("❌")
    print("sideinfobina.txt has non binary string")
    exit()
except:
    print("❌")
    exit()

print("2. Writing sideinfodeci.txt", end='\t')
try:
    with open("sideinfodeci.txt", "w") as f:
        f.write(buffer)
    print("✅")
except:
    print("❌")
    exit()
