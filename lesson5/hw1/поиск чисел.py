

string = str(input("введите число:"))
substring = str(input("введите что нужно найти:"))

cnt = string.count(substring)
if cnt >= 2:
    print("да есть повторения")
else:
    print("нет совпадений")
print("данное число повторяется", cnt, "раз" )
