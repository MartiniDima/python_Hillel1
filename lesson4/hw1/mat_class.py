a = int(input("введите количество учеников для класа A"))
b = int(input("введите количество учеников для класа B"))
c = int(input("введите количество учеников для класа C"))
#количество парт по класам которые будут заняты по два человека
aa = a // 2
bb = b // 2
cc = c // 2
# узнаем есть ли люди которые будут сидеть за партой в одиночку
aaa = a % 2
bbb = b % 2
ccc = c % 2
# сумма людей которые сидят за партой одни, сгрупируем их
y = aaa + bbb + ccc
j = y // 2 + y % 2
sum_part = aa + bb + cc + j
print("нужное количество парт для трех класов", sum_part)


#расчитаем количество парт для каждого класса по отдельности
print("количство парт в для каждого класса")
partA = a//2 + a % 2
partB = b//2 + b % 2
partC = c//2 + c % 2
print("для класса A", partA )
print("для класса B", partB)
print("для класса С", partC)