str = str(input("введите предложение:"))

s = list(str.split())
stroka_new = s
new_list = sorted(s)
l = len(new_list)

if l <= 2:
    stroka_new = str(input("введите больше двух слов:"))
else:
    print(s)
    print(new_list)
    print("количество слов в списке", l)
    for i in new_list:
        x = new_list.index(i)
        print( '{:<15}'.format(x), "{:>15}".format(i))
