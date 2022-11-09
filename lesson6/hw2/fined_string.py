f = str(input("введите слово или рядок:"))
c = str(input("введите символ который нужно найти в солве:"))
start = -1
count = 0
while True:
    start = f.find(c, start+1)
    if start == -1:
        break
    count += 1
print("количество вхождений составляет", count, "раз")
