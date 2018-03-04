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
  
 def carre_bis(a,b):
  X=[]
  Y=[]
  for i in range(a,b+1):
    X.append(i)
    Y.append(i**2)
  print(X)
  print(Y)
  
  def depasse_carre(M):
  V=0
  while V**2 < M:
    V = V + 1
  print(V)
