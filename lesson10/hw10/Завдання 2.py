import random

list = {x +10000 : x + random.randint(1,20) for x in range(20) for i in range(20)}
print(list)
print("Количестко значений словаря:", len(list))
print("Ключи:", list.values())
z = 1
for i in list.values():
    z *= i
print("произведение всех ключей словаря:", z)


