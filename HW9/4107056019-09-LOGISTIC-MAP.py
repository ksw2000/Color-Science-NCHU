import random as random
with open("input09.txt") as f:
	line = f.readline()
	x0, r, m, seed = line.strip("\n").split(" ")
	x0 = float(x0)
	r  = float(r)
	m  = int(m)
	seed = int(seed)
	random.seed(seed)

	logistic_list = []
	random_list = []

	x = x0
	for i in range(m):
		x = r * x * (1-x)
		logistic_list.append(x)
		random_list.append(random.random())

mean_l, mean_r = 0, 0
std_l, std_r = 0, 0
ret = 'x0, r, N, seed\n%f, %f, %d, %f\n' % (x0, r, m, seed)

i = 0
while i < m:
	ret += '%d, %f, %f\n' % (i+1,logistic_list[i],random_list[i])
	mean_l += logistic_list[i]
	mean_r += random_list[i]
	std_l += logistic_list[i] * logistic_list[i]
	std_r += random_list[i] * random_list[i]
	i = i + 1

mean_l /= m
mean_r /= m
std_l = (std_l / m - mean_l * mean_l) ** 0.5
std_r = (std_r / m - mean_r * mean_r) ** 0.5

ret += 'mean, %f, %f\n' % (mean_l, mean_r)
ret += 'std, %f, %f\n' % (std_l, std_r)

with open("output09.csv", 'w+') as f:
	f.write(ret)
