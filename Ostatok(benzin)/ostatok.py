__author__ = 'Alex'
"""программа вычисляет осататок бензина"""

probeg_na_torpede = 10000 #input()
probeg_v_putevke = 1000 #input()

posledniy_check = 1000 #float(input())
perviy_check = 100 #float(input())

ostatok_v_bake = 10 #float(input())
norma_rashoda = 0.09

run_for_a_month = probeg_na_torpede - probeg_v_putevke
rashod_po_spidometry = run_for_a_month * norma_rashoda

rashod_po_checkam = posledniy_check - perviy_check + ostatok_v_bake

ostatok = rashod_po_spidometry - rashod_po_checkam

#print(run_for_a_month)

"""Надо проверить потом"""