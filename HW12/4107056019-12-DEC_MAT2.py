import PIL.Image
import os
import numpy
import math

def NPCR(img1, img2):
    r, g, b = 0, 0, 0
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            r += 1 if img1[i][j][0] != img2[i][j][0] else 0
            g += 1 if img1[i][j][1] != img2[i][j][1] else 0
            b += 1 if img1[i][j][2] != img2[i][j][2] else 0
    nums = img1.shape[0] * img1.shape[1]
    return r*100/nums, g*100/nums, b*100/nums

def UACI(img1, img2):
    r, g, b = 0, 0, 0
    nums = img1.shape[0] * img1.shape[1]
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            r += abs(int(img1[i][j][0]) - int(img2[i][j][0]))
            g += abs(int(img1[i][j][1]) - int(img2[i][j][1]))
            b += abs(int(img1[i][j][2]) - int(img2[i][j][2]))

    return r*100/nums/255, g*100/nums/255, b*100/nums/255

ORIDIR = 'Origi_image'
ENCRYDIR = 'Encry_image'

lines = 'No, ORI Images, ENC Image, NPCR(R), NPCR(G), NPCR(B), UACI(R), UACI(G), UACI(B)\n'
count = 0
_, _, filenames = next(os.walk(ORIDIR))
for fn_ori in filenames:
    count += 1
    fnList = fn_ori.split(".")
    fn_enc = "%s_en.%s" % (fnList[0], fnList[1])
    img_ori = numpy.asarray(PIL.Image.open("%s/%s" % (ORIDIR, fn_ori)), dtype=numpy.int64)
    img_enc = numpy.asarray(PIL.Image.open("%s/%s" % (ENCRYDIR, fn_enc)), dtype=numpy.int64)
    line = '%d, %s, %s, ' % (count, fn_ori, fn_enc)
    line += '%.4f, %.4f, %.4f, ' % NPCR(img_ori, img_enc)
    line += '%.4f, %.4f, %.4f\n' % UACI(img_ori, img_enc)
    print(line)
    lines += line

with open("output12.csv", "w+") as f:
    f.write(lines)
