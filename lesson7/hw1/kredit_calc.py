sum = int(input("введите сумму кредита:"))
per = int(input("введите количество лет:"))
o_summa = sum
o_period = per * 12
o_procent = 2
o_procent2 = 4

ostat_summa = sum
ostat_period_mes = int(o_period)

opl_mes = 0
sum_proc = 0
while True:

        if opl_mes > 24 and opl_mes < o_period:
            opl_mes += 1
            plat_bez_procenta = ostat_summa / o_period
            ostat_summa -= plat_bez_procenta
            procent = plat_bez_procenta / 100 * o_procent2
            plata_s_procentom = plat_bez_procenta + procent
            sum_proc += procent
            print("месяц выплаты 4%", opl_mes,"сумма",  plata_s_procentom)

        if opl_mes <= 24 and opl_mes < o_period:
            ostat_period_mes -= 1
            opl_mes += 1
            plat_bez_procenta = ostat_summa/o_period
            ostat_summa -= plat_bez_procenta
            procent = plat_bez_procenta/100*2
            plata_s_procentom = plat_bez_procenta + procent
            sum_proc += procent
            print("месяц выплаты 2%", opl_mes,"сумма",  plata_s_procentom)







