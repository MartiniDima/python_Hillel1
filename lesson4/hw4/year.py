year = int(input("Введите год для проверки:"))

if year >= 1900 and year <= 1000000:
    print("Спасибо ")
    y = year
    if y % 4 == 0 and y % 400 == 0 and y % 100 == 0:
        print(y, "высокостный год")
    else:
        print(y, " НЕ высокостный год")
else:
    print("неверные параметры ввода")





