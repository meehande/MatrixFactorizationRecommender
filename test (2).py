import blc
#import cProfile
import timeit
#import time
#from memory_profiler import memory_usage
#import numpy as np
#import pylab as pl

n = 500
m = 100
d = 10
R = blc.createR(n,m,d)
W = blc.sampleR(R)


start_time = timeit.default_timer()

(U,V) = blc.ls(R,W,d)
#cProfile.run('(U,V) = ls(R,W,d)')
print timeit.default_timer()-start_time
#print np.dot(U.T,V)-np.dot(Ustar.T,Vstar)


start_time = timeit.default_timer()
(U,V) = blc.ls2(R,W,d)
print timeit.default_timer()-start_time

#print np.dot(U.T,V)-np.dot(Ustar.T,Vstar)

"""start_time = timeit.default_timer()
(U,V) = zero_mat_fact.ZeroMatFact(R,d)
print timeit.default_timer()-start_time"""


#MEMORY USAGE TESTS:
"""
mem = memory_usage((blc.ls, (R,W,d)))

x = np.linspace(0, len(mem) * .1, len(mem))

p = pl.fill_between(x, mem)

pl.xlabel('time')
pl.ylabel('Memory consumption (in MB)')
pl.show()"""
