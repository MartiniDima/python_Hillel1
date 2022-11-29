
n = int(input('n = '))

a = [[i if s % 2 == 0 else s +1 for i in range(-n, -0,)  ] for s in range(n)  ]
for j in a:
    j = str(j)
    print(j)


