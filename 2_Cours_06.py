# 2_Cours_06
# Probabilités

-----------------------------------------------------------------------------------------
import random as rd

def approx_pi(n):
# fourni une approximation de Pi en fonction d'un nombre d'essai de l'EA
# génération de 2 VA de loi uniforme sur [0,1] représentant les coordonnées
# comptage nombre de points dans le 1/4 de disque

  compteur = 0
  
  for i in range(n):
		X = rd.random()
		Y = rd.random()
		if X[i]**2 + Y[i]**2 < 1:
	    		compteur += 1

  print("Prob = ", round(compteur*4/n, 5))

---------------------------------------------------------------------------------------------

from math import sqrt
import random as rd

def approx_pi_2(n):
	compteur = 0

  for i in range(n):
	  X = rd.random()
	  Y = sqrt(1-X**2)
	  Z = rd.random()
	  if Z < Y:
	    compteur += 1
  
	print("Prob = ", round(compteur*4/n, 5))
