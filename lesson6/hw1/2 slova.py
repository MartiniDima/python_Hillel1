
while True:
    s = input("введите два слова через пробел:")

    if (s.find(" ")) == -1:
        pass
    else:
        print("отлично смотри что получилось")
        s = s[::-1]
        s = s.title()
        s = s.split(" ")
        s = s[::-1]
        print(s)