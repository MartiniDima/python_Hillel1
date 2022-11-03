N = int(input('N='))
c = 0
for (i) in range(1, N + 1):
    i *= i
    c += 1
    if str(c) in str(i):
        print(c, "*",c, "=",  i)
