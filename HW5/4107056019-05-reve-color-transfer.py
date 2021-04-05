import numpy as np
import cv2

def get12values(filePath):
	f = open(filePath, "r")
	return f.read().split('\n')

# @return src
def recover_color_transfer(result, values):
    lms = float(values[0])
    ams = float(values[1])
    bms = float(values[2])
    lds = float(values[3])
    ads = float(values[4])
    bds = float(values[5])
    lmt = float(values[6])
    amt = float(values[7])
    bmt = float(values[8])
    ldt = float(values[9])
    adt = float(values[10])
    bdt = float(values[11])

    result = cv2.cvtColor(result, cv2.COLOR_BGR2LAB).astype("float32")
    (l, a, b) = cv2.split(result)
    l = (l - lmt)*lds/ldt+lms
    a = (a - amt)*ads/adt+ams
    b = (b - bmt)*bds/bdt+bms

    l = _scale_array(l, clip=True)
    a = _scale_array(a, clip=True)
    b = _scale_array(b, clip=True)
    recorverd = cv2.merge([l, a, b])
    recorverd = cv2.cvtColor(recorverd.astype("uint8"), cv2.COLOR_LAB2BGR)
    return recorverd

def image_stats(image):
	(l, a, b) = cv2.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())

	# return the color statistics
	return (lMean, lStd, aMean, aStd, bMean, bStd)

def show_image(title, image, width=300):
	# resize the image to have a constant width, just to
	# make displaying the images take up less screen real
	# estate
	r = width / float(image.shape[1])
	dim = (width, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

	# show the resized image
	cv2.imshow(title, resized)

def _min_max_scale(arr, new_range=(0, 255)):
	"""
	Perform min-max scaling to a NumPy array

	Parameters:
	-------
	arr: NumPy array to be scaled to [new_min, new_max] range
	new_range: tuple of form (min, max) specifying range of
		transformed array

	Returns:
	-------
	NumPy array that has been scaled to be in
	[new_range[0], new_range[1]] range
	"""
	# get array's current min and max
	mn = arr.min()
	mx = arr.max()

	# check if scaling needs to be done to be in new_range
	if mn < new_range[0] or mx > new_range[1]:
		# perform min-max scaling
		scaled = (new_range[1] - new_range[0]) * (arr - mn) / (mx - mn) + new_range[0]
	else:
		# return array if already in range
		scaled = arr

	return scaled

def _scale_array(arr, clip=True):
	"""
	Trim NumPy array values to be in [0, 255] range with option of
	clipping or scaling.

	Parameters:
	-------
	arr: array to be trimmed to [0, 255] range
	clip: should array be scaled by np.clip? if False then input
		array will be min-max scaled to range
		[max([arr.min(), 0]), min([arr.max(), 255])]

	Returns:
	-------
	NumPy array that has been scaled to be in [0, 255] range
	"""
	if clip:
		scaled = np.clip(arr, 0, 255)
	else:
		scale_range = (max([arr.min(), 0]), min([arr.max(), 255]))
		scaled = _min_max_scale(arr, new_range=scale_range)

	return scaled

err = False
print("Reading...")
print("\t- sideinfodeci.txt", end='')
try:
	values = get12values("sideinfodeci.txt")
	print("\t✅")
except:
	err = True
	print("\t❌")

print("\t- utl1.png", end='')

result = cv2.imread("utl1.png")

if result is not None:
	print("\t\t✅")
else:
	err = True
	print("\t\t❌")

if not err:
	print("process...")
	recovered = recover_color_transfer(result, values)
	print("success...")
	show_image("Recovered source", recovered)
	show_image("Previous result", result)
	cv2.waitKey(0)
	cv2.imwrite("yrcsou.png", recovered)
	print("save recovered source image to yrcsou.png")
else:
	print("Something error 🙅‍")
