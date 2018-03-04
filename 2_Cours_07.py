# 2_Cours_07
# Parabole

def carre(a):
  X=[]
  Y=[]
  for i in range(a,5):
    X.append(i)
    Y.append(i**2)
  print(X)
  print(Y)
#-------------------------------------------------------
def carre_bis(a,b):
 X=[]
 Y=[]
 for i in range(a,b+1):
   X.append(i)
   Y.append(i**2)
 print(X)
 print(Y)
#---------------------------------------------------------- 
def depasse_carre(M):
  V=0
  while V**2 < M:
    V = V + 1
  print(V)
#-----------------------------------------------------------
def f(x):
  return a*x**2+b*x+c

def sommet_parabole():
  S=-100
  if a>0:
    for i in range(-100,101):
      if f(i)<f(S):
        S=i
    print("le sommet est à proximité du point:")     
    print("Sx = ",S)
    print("Sy = ",f(S))
  else:
    for i in range(-100,101):
      if f(i) > f(S):
        S=i
    print("le sommet est à proximité du point:")    
    print("Sx = ",S)
    print("Sy = ",f(S))
    
a = eval(input(" a = "))
b = eval(input(" b = "))
c = eval(input(" c = "))
sommet_parabole()
#--------------------------------------------------
# Algorithme de Dichotomie :
import math

def f(x):
  return x **3+x -1

def dichotomie(a, b, f, epsilon = 1e-6) :
  if( math.fabs (a - b) <= epsilon ):
    return (a+b) /2.0
  else :
    fa = f(a)
    fb = f(b)
    fab = f((a+b) /2.0)
    if(fa * fab <= 0):
      return dichotomie (a, (a+b)/2.0 , f, epsilon )
    elif (fab * fb <= 0):
      return dichotomie ((a+b)/2.0 , b, f, epsilon )
    else :
      raise Exception (" Domaine invalide pour trouver un zéro par dichotomie ")

a = 0
b = 1
print (" Zéro de x**3+x-1 sur [{} ,{}] : {}". format (a, b, round ( dichotomie (a, b , f) ,6))
#-----------------------------------------------------------------------------------------------

