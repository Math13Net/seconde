# 2_Cours_09
# Equation de droite - Système

--------------------------------------------------------------------------------------
from math import *

def droite_2_points(xa,ya,xb,yb):
# affiche l'équation d'une droite lorsque l'on fournit 2 points

  if xa != xb:
    a = (yb-ya)/(xb-xa)
    b = ya -a*xa
    print("l'équation de la droite est : y = ",a,"x + ",b)
  else:
    print("l'équation de la droite est : x = ",xa)
    
----------------------------------------------------------------------------------    
