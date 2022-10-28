

string = int(input("введите число:"))
substring = int(input("введите что нужно найти:"))

cnt = string.count(substring)
if cnt >= 2:
    print("да есть повторения")
else:
    print("нет совпадений")
print("данное число повторяется", cnt, "раз" )
