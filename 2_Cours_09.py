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
from math import *

def droite_2_points(xa,ya,xb,yb):
# étudie la position relative de 2 droites : parallèles, perpendiculaires ou donne le point d'intersection  
  if xa != xb:
    a = (yb-ya)/(xb-xa)
    b = ya -a*xa
    print("l'équation de la droite est : y = ",a,"x + ",b)
  else:
    print("l'équation de la droite est : x = ",xa)
    
def position_droite(a1,b1,a2,b2):
  if a1==a2:
    print("les 2 droites sont parallèles")
  elif a1*a2==-1:
    print("les 2 droites sont perpendiculaires")
  else:
    x = (b2-b1)/(a1-a2)
    y = a1*(b2-b1)/(a1-a2)+b1
    print("(",x,",",y,") est le point d'intersection des 2 droites")
