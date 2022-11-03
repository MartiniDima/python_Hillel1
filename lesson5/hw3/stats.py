n = []
f = int(input("введите цыфры:"))
while f > 0:
    f = int(input("введите цыфры:"))
    n.append(f)
print(n)


sum = 0
kolichestvo = 0
parn = 0
nparn = 0

for i in n:
    if i >= 0:
        sum +=i
        kolichestvo += 1
    if i % 2 == 0:
        parn += 1
    if i % 2 != 0:
        nparn += 1

print("сумма всех чисел в списке", sum)
print ("среднее арифметическое", sum / kolichestvo)
print("максимальное число в списке", max(n))
print("минимальное число в списке", min(n))
print("количество парных чисел", parn)
print("количество не парных чисел", nparn)