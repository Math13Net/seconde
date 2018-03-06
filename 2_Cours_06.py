# 2_Cours_06
# Probabilités

------------------------------------------------------------------------------------------------
import random as rd

def approx_pi_1(n):
# génère 2 VA uniforme X et Y sur [0,1] faisant office de coordonnées
# il suffit de vérifier si le point est dans le 1/4 de disque

  compteur = 0
  for i in range(n):
	  X = rd.random()
	  Y = rd.random()
	  if X[i]**2 + Y[i]**2 < 1:
	    compteur += 1
  print("Prob = ", round(compteur*4/n, 5))

------------------------------------------------------------------------------------------------
from math import sqrt
import random as rd

def approx_pi_2(n):
# génère 1 VA uniforme X sur [0,1], faisant office d'abscisse
# on calcule l'ordonnée Y sur le disque associé, ce qui donne 1 point du cercle 
# génère 1 VA uniforme Z sur [0,1], faisant office d'abscisse de point
# par la méthode du rejet, on voit si le point est sous le cercle (dont dans le 1/ de disque)

  compteur = 0
  for i in range(n):
	  X = rd.random()
	  Y = sqrt(1-X**2)
	  Z = rd.random()
	  if Z < Y:
	    compteur += 1
  print("Prob = ", round(compteur*4/n, 5))
