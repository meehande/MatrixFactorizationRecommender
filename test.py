import numpy as np
from numpy import linalg as nlin
import cProfile
import timeit
from scipy import linalg as slin

def ls(R,W,d):
  (n,m) = R.shape
  sigma = 0.0001
  Id = np.identity(d)
  U0 = np.zeros((d,n))
  
  V = np.random.rand(d, m)
  for i in range(1000):
      U = U0
      for g in range(n):
          VV = np.zeros(d)
          for w in W[g]:
             VV = VV+np.dot(V[:,w],V[:,w].T)
          X = nlin.pinv(sigma*Id+VV)
          #X = sigma*Id + VV
          for v in W[g]:
             U[:,g] = U[:,g] + R[g,v]*np.dot(V[:,v].T,X)               
             #U[:,g] = U[:,g] + R[g,v]*slin.solve(X ,V[:,v].T)
  
      Y = np.dot(U,U.T)
      Y = nlin.pinv(sigma*Id+Y)
      Y = np.dot(U.T,Y)
      #Y = np.linalg.solve( U.T, sigma*Id+Y)
      #Y = np.linalg.lstsq(U.T, sigma*Id+Y)
      for v in range(m):
         V[:,v] = np.dot(R[:,v].T,Y)

  return (U,V)

def ls2(R,W,d):
  (n,m) = R.shape
  sigma = 0.0001
  U = np.random.rand(d,n)
  V = np.random.rand(d,m)
  Id = np.identity(d)
  for i in range(1000):
    for g in range(n):
        # min (V'U - R')^2 by solving inv(VV')VR'
        t1 = np.dot(V, V.T) + Id*sigma
        t2 = np.dot(V, R[g].T)
        U[:,g] = np.linalg.solve(t1,t2)

    for v in range(m):
        # min (U'V - R)^2 by solving inv(UU')UR
        t1 = np.dot(U, U.T) + Id*sigma
        t2 = np.dot(U, R[:,v])
        V[:,v] = np.linalg.solve(t1, t2)
  return (U,V)

n = 100
m = 5
d = 2
Ustar = np.random.rand(d, n)
Vstar = np.random.rand(d, m)
R = np.dot(Ustar.T,Vstar)
#O = np.random.rand(n,m)
#R[O>1] = 0
W=[]
for i in range(n):
   W.append([])
   for j in range(m):
      W[i].append(j)

start_time = timeit.default_timer()
(U,V) = ls(R,W,d)
print timeit.default_timer()-start_time
#print np.dot(U.T,V)-np.dot(Ustar.T,Vstar)

start_time = timeit.default_timer()
(U,V) = ls2(R,W,d)
print timeit.default_timer()-start_time
#print np.dot(U.T,V)-np.dot(Ustar.T,Vstar)


