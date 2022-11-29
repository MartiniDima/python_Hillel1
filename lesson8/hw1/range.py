n = range(10, 250)
spis = []
form_spis = []
for i in n:
    spis.append(i)
for v in spis:
     if v%20 == 0:
        form_spis.append(v)


print(spis)
print(form_spis)