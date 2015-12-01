# -*- coding: utf-8 -*-
import numpy
from scipy import sparse as sps
#import scipy
import cProfile

def ls():
  n = 5
  m = 7
  d = 2
  sigma = 0.0001
  Ustar = numpy.random.rand(d, n)
  Vstar = numpy.random.rand(d, m)
  R = numpy.dot(Ustar.T,Vstar)
  O = numpy.random.rand(n,m)
  #R[O>1] = 0
  W=[]
  for i in range(n):
     W.append([])
     for j in range(m):
        W[i].append(j)

  Id = numpy.identity(d)
  U0 = numpy.zeros((d,n))

  V = numpy.random.rand(d, m)
  for i in range(1000):
      U = U0
      for g in range(n):
          VV = numpy.zeros(d)
          for w in W[g]:
             VV = VV+numpy.dot(V[:,w],V[:,w].T)
          X = numpy.linalg.pinv(sigma*Id+VV)
          for v in W[g]:
             U[:,g] = U[:,g] + R[g,v]*numpy.dot(V[:,v].T,X)

      Y = numpy.dot(U,U.T)
      Y = numpy.linalg.pinv(sigma*Id+Y)
      Y = numpy.dot(U.T,Y)
      for v in range(m):
         V[:,v] = numpy.dot(R[:,v].T,Y)

  print numpy.dot(U.T,V)-numpy.dot(Ustar.T,Vstar)
  return

cProfile.run('ls()','restats')
#ls()
