n = int(input("введите количество школьников:"))
k = int(input("введите количество яблок:"))
#количество яблок каждому школьнику
kol_j = k//n
korzinka = k % n
print("каждый школьник получит по ", kol_j, "яблок")
print("в корзинке останется", korzinka, "яблок")
