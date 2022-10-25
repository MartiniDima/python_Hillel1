year = int(input("Введите год для проверки:"))

if year >= 1900 and year <= 1000000:
    print("Спасибо ")
else:
    print("неверные параметры ввода")

if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
    print(year, "высокостный год")
else:
    print(year, " НЕ высокостный год")



#