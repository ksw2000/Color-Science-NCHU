from PIL import Image
import numpy as np

output = ""
with open("ART-DEC-input08.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        line = line.rstrip().split(" ")
        filename = line[0]
        art = (line[1] == '+')
        perioid = int(line[2])

        im = np.array(Image.open(filename))
        im2 = np.copy(im)
        N = im.shape[0]

        a, b, c, d = (1, 1, 1, 2) if art else (2, -1, -1, 1)

        for i in range(perioid-1):
            a, b, c, d = (a+c, b+d, a+2*c, c+2 *
                          d) if art else (2*a-c, 2*b-d, -a+c, -b+d)
        
        for s in range(N):
            for t in range(N):
                smap, tmap = (a * s + b * t) % N, (c * s + d * t) % N
                im2[smap][tmap] = im[s][t]

        saved = line[0].split("_")[1]
        Image.fromarray(im2).save(saved)
        output = output + saved + "\n"
        line = f.readline()

with open("ART-DEC-ouput08.txt", "w+") as f:
    f.write(output)
