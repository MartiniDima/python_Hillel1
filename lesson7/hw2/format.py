s = int(input("введите число:"))
con = 0
peremenna, nul = ["1", "0"]
num = 1
while con < s:
    if con != s:
        con +=1
        x = "{}{}".format(peremenna, nul*con)
        print(con, "{:>20}".format(x))

else:
    pass
