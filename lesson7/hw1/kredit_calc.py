sum = int(input("введите сумму кредита:"))
per = int(input("введите количество лет:"))
o_summa = sum/100*80
o_period = per * 12
o_procent = 0.25
o_procent2 = 0.25
print(o_summa)
ostat_summa = o_summa
ostat_period_mes = int(o_period)
pr = 0
opl_mes = 0
sum_proc = 0

while True:

    if opl_mes <= 23 and opl_mes < o_period :
        ostat_period_mes -= 1
        opl_mes += 1
        plat_bez_procenta = ostat_summa / o_period
        ostat_summa -= plat_bez_procenta
        procent = plat_bez_procenta / 100 * 2
        pr += procent
        plata_s_procentom = plat_bez_procenta + procent
        sum_proc += procent
        print("месяц выплаты   %.f " % (opl_mes), "сумма %.2f" % (plata_s_procentom),
              f" {o_procent:>10}% в месяц ")

    elif opl_mes >= 24 and opl_mes < o_period:

            opl_mes += 1
            plat_bez_procenta = ostat_summa / o_period
            ostat_summa -= plat_bez_procenta
            procent = plat_bez_procenta / 100 * o_procent2
            pr += procent
            plata_s_procentom = plat_bez_procenta + procent
            sum_proc += procent
            print("месяц выплаты   %.f " % (opl_mes), "сумма %.2f" % (plata_s_procentom),
                  f" {o_procent2:>10}% в месяц "

                  )


