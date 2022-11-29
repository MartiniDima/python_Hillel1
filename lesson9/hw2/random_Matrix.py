import random

n = int(input('n = '))
a = [[random.randint(1, 100) for d in range(n)]for i in range(n)]
y = len(a)
for i in range(n):
    print(a[i])

sum_ = 0
sum_ost = 0
for z in range(n):
    sum_ost += a[z][y - 1]
    for j in range(n):
        if z == j:
            sum_ += a[z][j]



print("Сумма последнего столбца :", sum_ost)

print("Сумма по диагонали составила :", sum_)
