import numpy
from scipy import sparse as sps

n = 5
m = 7
d = 2
"""
U_matrix = 5*numpy.random.rand(d, n)
V_matrix = 5*numpy.random.rand(d, m)"""
R_matrix = sps.rand(n,m, density = 0.5)
#here: logical matrix of 0/1s - R.todense()>0 -
R_matrix.tocsr()
print "R: ", R_matrix.todense()

U_matrix = 5*numpy.random.rand(d, n)
V_matrix = 5*numpy.random.rand(d, m)
#print "U: ", U_matrix
#print "V: ", V_matrix

for i in range(1000):
    for u in range (n):
        U_matrix[:, u] = numpy.dot(numpy.dot(R_matrix.todense()[u, :], V_matrix.T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(V_matrix, V_matrix.T))))

    for v in range(m):
        V_matrix[:, v] = numpy.dot(numpy.dot(R_matrix.todense()[:, v].T, U_matrix.T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(U_matrix, U_matrix.T))))

    R_tilde = numpy.dot(U_matrix.T, V_matrix)

    if i%50 == 0:
        print "R_tilde ", i, R_tilde
print "R_tilde ", i, R_tilde
def compare_matrices(a, b, tolerance):
    if a.shape != b.shape:
        return "different dimensions"
    n, m = a.shape
    for row in range(n):
        for column in range(m):
            if a[row, column] - b[row, column] > tolerance:
                return False
    return True

print compare_matrices(R_matrix.todense(), R_tilde, 0.001)
