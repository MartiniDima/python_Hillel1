import random

list = [random.randint(1, 15) for i in range(15)]
print(list)
p = 0
np = 0
for i in list:
    if i % 2 == 0:
        p +=i
    if i % 2 != 0:
        np +=i
if np > p:
    print("ТАК")
else:
    print("НІ")
