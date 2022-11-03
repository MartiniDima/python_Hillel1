
n = int(input("введите число для умножения:"))
c = 0
spis = []
for (i) in range(0, n + 1):
    c = i**2
    if (c) <= (n):
        spis.append(c)
        print (n, spis)