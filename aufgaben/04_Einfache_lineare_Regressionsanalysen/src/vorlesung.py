import math
#Übungsaufgabe aus Vorlesung:
echte_preise = [150, 200, 180, 750, 800, 1200, 130, 210, 1150, 780]
vorhergesagte_preise = [160, 205, 185, 760, 780, 1180, 140, 215, 1100, 770]
ss_res = 0

for pos in range(0, len(echte_preise)):
    ss_res = ss_res + ((echte_preise[pos] - vorhergesagte_preise[pos]) * echte_preise[pos] - vorhergesagte_preise[pos])

rse = math.sqrt((1/(len(echte_preise) - 2))* ss_res)
print("RSE: ", rse)

#ss_tot = 0
#for pos in range(0, len(echte_preise)):
#    ss_tot = math.pow(,2)
#rse = 21,722
#mse = 377?
#r^2 = 0,997