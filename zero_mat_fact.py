
import numpy as np

def ZeroMatFact(R, d):
    n,m = R.shape
    U_matrix = np.empty((d, n))
    V_matrix = np.random.rand(d, m)
    Id = np.identity(d)
    sigma = 0.0001
    
    for i in xrange(100):
        for u in range (n): # u = row
            #try:
            U_matrix[:, u] = np.dot(np.dot(R[u,R[u,:]!=0], V_matrix[:,R[u,:]!=0].T), np.linalg.pinv(np.asmatrix(Id*sigma + np.dot(V_matrix[:,R[u,:]!=0], V_matrix[:,R[u,:]!=0].T))))
            
    
        for v in range(m): #for each row
            V_matrix[:, v] = np.dot(np.dot(R[R[:,v]!=0, v].T, U_matrix[:, R[0:n,v]!=0].T), np.linalg.pinv(np.asmatrix(Id*sigma + np.dot(U_matrix[:, R[0:n,v]!=0], U_matrix[:, R[0:n,v]!=0].T))))
    
    return (U_matrix, V_matrix)