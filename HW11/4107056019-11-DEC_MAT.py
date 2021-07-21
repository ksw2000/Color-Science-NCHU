import PIL.Image
import os
import numpy
import math

# @param rgb 3D-list
# @return float64 mean_r, float64 mean_g, float64 mean_b
def mean(rgb):
    sum_r, sum_g, sum_b = 0, 0, 0
    for row in rgb:
        for column in row:
            sum_r += column[0]
            sum_g += column[1]
            sum_b += column[2]
    num_px = rgb.shape[0]*rgb.shape[1]
    return sum_r/num_px, sum_g/num_px, sum_b/num_px

# @param rgb 3D-list
# @return float64 zr, float64 zg, float64 zb
def getZ(rgb):
    zr = []
    zg = []
    zb = []
    # init
    for _ in range(256):
        zr.append(0)
        zg.append(0)
        zb.append(0)

    for row in rgb:
        for column in row:
           zr[column[0]] += 1
           zg[column[1]] += 1
           zb[column[2]] += 1
    return zr, zg, zb

# @param rgb 3D-list
# @return float64 variances_histogram_r (aka vhr), float64 vhg, float64 vhb
def variancesOfHistogram(rgb):
    zr, zg, zb = getZ(rgb)
    vhr, vhg, vhb = 0, 0, 0
    for i in range(256):
        for j in range(256):
            vhr += (zr[i] - zr[j]) ** 2
            vhg += (zg[i] - zg[j]) ** 2
            vhb += (zb[i] - zb[j]) ** 2
    # 256 * 256 * 2 = 131072
    return vhr / 131072.0, vhg / 131072.0, vhb / 131072.0

# @param rgb 3D-list
# @return float64 sannonEntropy_r (aka ser), float64 seg, float64 seb
def shannonEntropy(rgb):
    zr, zg, zb = getZ(rgb)
    ser, seg, seb = 0, 0, 0
    numOfPx = rgb.shape[0] * rgb.shape[1]
    for i in range(256):
        pr, pg, pb = zr[i] / numOfPx, zg[i] / numOfPx, zb[i] / numOfPx
        ser += 0 if pr == 0 else pr * math.log(pr, 2)
        seg += 0 if pg == 0 else pg * math.log(pg, 2)
        seb += 0 if pb == 0 else pb * math.log(pb, 2)
    return -ser, -seg, -seb

dir = ["Origi_image", "Encry_image", "Decry_image"]
out = ["output11.csv", "output11_en.csv", "output11_de.csv"]

# calculate the max length of filenamx
step, maxLen = 0, 0
while step < len(dir):
    _, _, filenames = next(os.walk(dir[step]))
    for f in filenames:
        if len(f) + len(dir[step]) > maxLen:
            maxLen = len(f)+len(dir[step])
    step += 1

# main program: open image and calculate mean value, 
# variance of histogram and shannon entropy
step, maxLen = 0, maxLen + 16
while step < len(dir):
    _, _, filenames = next(os.walk(dir[step]))

    lines = 'No,Images,MIR,MIG,MIB,VHR,VHG,VHB,SER,SEG,SEB\n'
    lineCounter = 0
    for f in filenames:
        print("%-*s" % (maxLen, dir[step]+"/"+f+""), end='')

        lineCounter += 1
        rgb = numpy.asarray(PIL.Image.open(dir[step]+"/"+f))
        line = "%d,%s," % (lineCounter, f)
        line += "%.2f,%.2f,%.2f," % mean(rgb)
        line += "%.2f,%.2f,%.2f," % variancesOfHistogram(rgb)
        line += "%.6f,%.6f,%.6f\n" % shannonEntropy(rgb)

        lines += line
        print("✔️")

    with open(out[step], "w+") as f:
        f.write(lines)

    step += 1
