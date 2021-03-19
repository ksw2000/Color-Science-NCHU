def factorial(i):
    ret = 1
    for i in range(1, i+1):
        ret *= i
    return ret


def c(p, q):
    if p < q:
        return 0
    j = 1
    for i in range(q+1, p+1, 1):
        j = j * i
    return j // factorial(p-q)

print('please input n k m')
n2, k2, m2 = input().split()
n = int(n2)
k = int(k2)
m = int(m2)
if n < 1 or n > 81 or k < 1 or k > n or m < 0 or m > c(n,k)-1:
    print("Error (1<=n<=81 1<=k<=n 0<=m<=C(n,k)-1)")
    exit()

r = m
s = []
j = n
for step in range(k):
    i = j-1
    while i >= k-1-step:
        # decreasing order
        if c(i, k-step) <= r:
            break
        i = i-1
    j = i
    s.append(i)
    r = r-c(j, k-step)

print(s)