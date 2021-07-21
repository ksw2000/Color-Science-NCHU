import PIL.Image
import os
import numpy

ORIDIR = 'Origi_image'
ENCRYDIR = 'Encry_image'

# @param 3D nparray
# @return (x[[r,g,b][r,g,b]...] y[[r,g,b][r,g,b]...])
def getHD(img):
    cols = img.shape[1]
    return img[:, 0:cols-1, :].reshape(-1, 3), img[:, 1:cols, :].reshape(-1, 3)

def getVD(img):
    rows = img.shape[0]
    return img[0:rows-1, :, :].reshape(-1, 3), img[1:rows, :, :].reshape(-1, 3)

def getDD(img):
    cols = img.shape[1]
    rows = img.shape[0]
    return img[0:rows-1, 0:cols-1, :].reshape(-1, 3), img[1:rows, 1:cols, :].reshape(-1, 3)

# @param 2D nparray list
def mean(list):
    sum = numpy.asarray([.0, .0, .0], dtype=numpy.float64)
    for px in list:
        sum = sum + px
    return sum / len(list)

# @param 2D nparray list (x or y)
# @param 2D nparray mean (mean x or mean y)
def var(list, mean):
    sum = numpy.asarray([.0, .0, .0], dtype=numpy.float64)
    for px in list:
        sum += numpy.square(px - mean)
    return sum / (len(list) - 1)

def cov(x, y, x_mean, y_mean):
    sum = numpy.asarray([.0, .0, .0], dtype=numpy.float64)
    for i in range(len(x)):
        sum += (x[i] - x_mean) * (y[i] - y_mean)
    return sum / (len(x) - 1)

def correlation(cov_xy, var_x, var_y):
    # correlation(x, y) = cov(x, y) / sqrt(var(x)) / sqrt(var(y))
    return cov_xy / (numpy.sqrt(var_x) * numpy.sqrt(var_y))
    
def work(fn, mode, x, y):
    mx, my = mean(x), mean(y)
    varx, vary = var(x, mx), var(y, my)
    covar = cov(x, y, mx, my)
    coco = correlation(covar, varx, vary)

    line = ''
    i = 0
    for rgb in ['R', 'G', 'B']:
        line += '%s,%s,%s CHANNEL,' % (fn, mode, rgb)
        line += '%.2f,%.2f,%.2f,' % (mx[i], my[i], varx[i])
        line += '%.2f,%.2f,%.6f\n' % (vary[i], covar[i], coco[i])
        i += 1

    return line

lines = 'Image Name,Mode,Channel,MEAN(x),MEAN(y),VAR(X),VAR(Y),"COV(X,Y)","Correlation(X,Y)"\n'
_, _, filenames = next(os.walk(ORIDIR))
_, _, filenames2 = next(os.walk(ENCRYDIR))
for fn_ori in filenames:
    fnList = fn_ori.split(".")
    fn_enc = "%s_en.%s" % (fnList[0], fnList[1])
    img_ori = numpy.asarray(PIL.Image.open(
        "%s/%s" % (ORIDIR, fn_ori)), dtype=numpy.int64)
    img_enc = numpy.asarray(PIL.Image.open(
        "%s/%s" % (ENCRYDIR, fn_enc)), dtype=numpy.int64)

    x, y = getHD(img_ori)
    lines += work(fn_ori, 'HD', x, y)
    x, y = getVD(img_ori)
    lines += work(fn_ori, 'VD', x, y)
    x, y = getDD(img_ori)
    lines += work(fn_ori, 'DD', x, y)
    x, y = getHD(img_enc)
    lines += work(fn_enc, 'HD', x, y)
    x, y = getVD(img_enc)
    lines += work(fn_enc, 'VD', x, y)
    x, y = getDD(img_enc)
    lines += work(fn_enc, 'DD', x, y)

with open("output13.csv", "w+") as f:
    f.write(lines)
