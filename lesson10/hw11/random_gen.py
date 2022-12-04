import random
list = [random.randint(1,20) for i in range(20)]
print('рандомный список:', list)
set = set(list)
print("все разные символы:", set)
cont = 0
for i in set:
    cont += 1
print("разних чисел встречается :",cont)