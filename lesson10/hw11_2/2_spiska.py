spis_1 = [3, 3, 4, 7, 8, 90, 23, 0]
spis_2 = [56, 23, 1, 3, 4, 7, 1, 0, 5, 3, 3, 3, 4,3, 6]

print("количествоне повторяющихся чисел в двух списках составло:", len([i for i in set(spis_1 + spis_2)]))