from PIL import Image
import numpy as np

output = ""
with open("ART-ENC-input08.txt") as f:
    line = f.readline()
    while line:
        line = line.rstrip().split(" ")
        filename = line[0]
        art = (line[1] == '+')
        perioid = int(line[2])
        
        im = np.array(Image.open(filename))
        im2 = np.copy(im)
        N = im.shape[0]

        count = 1
        a, b, c, d = (1, 1, 1, 2) if art else (2, -1, -1, 1)
        thisPeriod = False
        while not thisPeriod:
            thisPeriod = True
            # encrypt mode
            if count == perioid:
                for s in range(N):
                    for t in range(N):
                        smap, tmap = (a * s + b * t) % N, (c * s + d * t) % N
                        im2[smap][tmap] = im[s][t]

            # finding period mode
            for s in range(N):
                for t in range(N):
                    smap, tmap = (a * s + b * t) % N, (c * s + d * t) % N
                    if (smap != s) or (tmap != t):
                        thisPeriod = False
                        break
                if not thisPeriod:
                    count += 1
                    a, b, c, d = (a+c, b+d, a+2*c, c+2*d) if art else (2*a-c, 2*b-d, -a+c, -b+d)
                    break

        # encrypt done and peroid found, output the result
        saved = "ART" + line[1] + line[2] + "_" + line[0]
        Image.fromarray(im2).save(saved)
        output = output + saved + " " + str(count) + "\n"
        line = f.readline()

with open("ART-ENC-ouput08.txt", "w+") as f:
    f.write(output)
