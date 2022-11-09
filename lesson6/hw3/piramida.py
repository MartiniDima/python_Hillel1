
var = int(input("введите число"))
if var >= 3 and var <= 9:
    for i in range(1, var + 2):
        for j in range(1, i -1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()