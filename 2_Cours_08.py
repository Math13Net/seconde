# 2_Cours_08
# Echantillonnage - Fluctuation

------------------------------------------------------------------------------------------------
# Intervalle de fluctuation
# 1 EA = 1 Echantillon = 150 lancés de dés puis comptage du nombre de 5
# le graphe représente 100 EA donc 100 échantillons
# en abscisse, le numéro de l'échantillon
# en ordonnée, le nombre de 5 par échantillon
# on regarde la fluctuation des échantillons entre 15 et 25

from math import *
from random import *
import matplotlib as mpl
import matplotlib.pyplot as plt

# initialisation
taille = int(input("taille des échantillons ="))
nombre = int(input("nombre d'échantillons ="))
min = int(input("nombre minimum de 5 ="))
max = int(input("nombre maximun de 5 ="))
nombre_echantillon_entre_15_et_25 = 0
tirage = []

# realisation de l'experience
for i in range(nombre):
  nombre_5 = 0
  for j in range(taille):
    x=randint(1,6)
    if x==5:
      nombre_5+=1
  tirage.append(nombre_5)
  if nombre_5<=max and nombre_5>=min:
    nombre_echantillon_entre_15_et_25 +=1

# affichage des résultats
print("Nombre d'échantillon entre 15 et 25 = ",nombre_echantillon_entre_15_et_25)
print("pourcentage = ",nombre_echantillon_entre_15_et_25/nombre*100,"%")

# tracé du graphe
fig = plt.figure()

numero = [i+1 for i in range(nombre)]
ligne_min = [min for i in range(nombre)]
ligne_max = [max for i in range(nombre)]

plt.plot(numero, tirage, "gs", )
plt.plot(numero, ligne_min, "b", linewidth=1)
plt.plot(numero, ligne_max, "r", linewidth=1)

plt.title('Réalisation des %i échantillons de %i tailles' %(nombre,taille))
plt.xlabel('numéro échantillon')
plt.ylabel('nombre de 5 dans échantillon')
plt.axis([0, nombre+1, 0, taille/2])

plt.text(nombre+3, min-2, r'%s'%(min))
plt.text(nombre+3, max-2, r'%s'%(max))
plt.text(nombre/2-20, max+20, r'Taux entre %s et %s = %s' %(min,max,round(nombre_echantillon_entre_15_et_25/nombre*100,2)))

plt.annotate('1 échatillon = %s lancés' %(taille), xy=(nombre/2, (min+max)/2), xytext=(nombre/2+10, max+10), arrowprops={'facecolor':'black', 'shrink':0.05} )

plt.savefig("graph.png")
