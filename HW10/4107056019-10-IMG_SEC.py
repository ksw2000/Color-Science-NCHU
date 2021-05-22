import random as random
import math as math
from decimal import *

try:
    with open("./Input10.txt", "r") as f:
        x0, rx  = f.readline().strip().split(' ')
        y0, ry  = f.readline().strip().split(' ')
        seed, N = f.readline().strip().split(' ')
        L = f.readline().strip()
except:
    print("open('./Input10.txt') error")
    exit()

_x0, _rx, _y0, _ry, _L = float(x0), float(rx), float(y0), float(ry), float(L)

random.seed(int(seed))
r1, r2, r3 = random.randint(1, int(N)), random.randint(1, int(N)), random.randint(1, int(N))

xn, yn = _x0, _y0

for _ in range(r1):
    xn = _rx * xn * (1 - xn)

for _ in range(r2):
    yn = _ry * yn * (1 - yn)

a, b = math.ceil(xn/_L) + r1, math.ceil(yn/_L) + r2

res  = '%s %s\n%s %s\n%s %s\n%s\n' % (x0, rx, y0, ry, seed, N, L)
res += '%d %d %d\n' % (r1, r2, r3)
res += '%s %s\n' % (format(Decimal.from_float(xn), '.21'), format(Decimal.from_float(yn), '.21'))
res += '%d %d' % (a, b)

with open("Output10.txt", "w+") as f:
    f.write(res)

print(res)