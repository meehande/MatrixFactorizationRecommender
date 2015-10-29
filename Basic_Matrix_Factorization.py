import random
import numpy

iterations = 5
sigma_rat = 0
rank = 2
n = 10
m = 100
d = 2
sigma = 0


#correct matrix we want to get back to
U_matrix = 5*numpy.random.rand(d, n)

V_matrix = 5*numpy.random.rand(d, m)

# R_matrix = numpy.matrix('1,2,;3,5')
R_matrix = numpy.dot(U_matrix.T, V_matrix)
print "1st U: \n", U_matrix
print "1st V: \n", V_matrix

print "original R: \n", R_matrix

R_tilde = numpy.matrix('0,0 ; 0,0')


# begin with random guesses of what could give R
U_matrix = 5*numpy.random.rand(d, n)

V_matrix = 5*numpy.random.rand(d, m)
print "2nd U: \n", U_matrix
print "2nd V: \n", V_matrix


for i in range(iterations):
    for u in range (n): # u = row
        U_matrix[:, u] = numpy.dot(numpy.dot(R_matrix[u, :], V_matrix.T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(V_matrix, V_matrix.T))))
        # U_matrix = numpy.linalg.solve(numpy.dot(V_matrix,V_matrix.T)+ sigma_rat*numpy.eye(2), numpy.dot(V_matrix, R_matrix.T)).T
        # U_matrix[u,:] = numpy.linalg.solve(numpy.dot(V_matrix[:, u].T, V_matrix[:, u])+sigma_rat*numpy.eye(2), numpy.dot(V_matrix[u, :].T, R_matrix[u, :]))
        # IS Ruv A SCALAR??

    for v in range(m): #for each row
        # V_matrix = numpy.linalg.solve(numpy.dot(U_matrix.T,U_matrix)+ sigma_rat*numpy.eye(2), numpy.dot(U_matrix.T, R_matrix))
        # V_matrix[:,v] = numpy.linalg.solve(numpy.dot(U_matrix.T, U_matrix) + sigma_rat*numpy.eye(2), numpy.dot(U_matrix.T, R_matrix[:, v].T)).T
        V_matrix[:, v] = numpy.dot(numpy.dot(R_matrix[:, v].T, U_matrix.T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(U_matrix, U_matrix.T))))

    R_tilde = numpy.dot(U_matrix.T, V_matrix)

print "ANSWER:\n", R_tilde


def compare_matrices(a, b, tolerance):
    if a.shape != b.shape:
        return "different dimensions"
    n, m = a.shape
    for row in range(n):
        for column in range(m):
            if a[row, column] - b[row, column] > tolerance:
                return False
    return True

print compare_matrices(R_matrix, R_tilde, 0.1)

"""
for i in range (iterations):
    U_matrix = numpy.linalg.solve(numpy.dot(R_matrix, V_matrix.T),numpy.linalg.inv(numpy.dot(V_matrix, V_matrix.T) + sigma_rat*numpy.eye(rank)))
    print "U matrix"
    print U_matrix

    V_matrix =  numpy.linalg.solve(numpy.dot(R_matrix, U_matrix.T),numpy.linalg.inv(numpy.dot(U_matrix, U_matrix.T) + sigma_rat*numpy.eye(rank)))
    print "V matrix"
    print V_matrix

    R_tilde = numpy.dot(U_matrix, V_matrix.T)

    print "R tilde"
    print R_tilde
"""

""" copying matlab..."""
"""
UUU = numpy.eye(rank) / sigma
VVV = numpy.eye(rank) / sigma
n = 2 #num users - matrix dimension
for i in range (iterations):
    for g in range(n):
        U_matrix[:, g] = numpy.dot(R_matrix[g, :],  V_matrix[:, g].T)/numpy.dot((VVV + V_matrix), V_matrix.T)
#Unetflix(:,g) =  R(g,existingvalues(g,:)) * Vnetflix(:,(existingvalues(g,:)))' / (VVVnetflix+Vnetflix(:,(existingvalues(g,:))) * Vnetflix(:,(existingvalues(g,:)))');

    for v in range(n):
        V_matrix[:, v] = numpy.dot(R_matrix[:, v].T,  U_matrix[:, g].T)/numpy.dot((UUU + U_matrix), U_matrix.T)
#Vnetflix(:,v) = R(existingvalues(:,v),v)' * Unetflix(:,existingvalues(:,v))' / (UUUnetflix + Unetflix(:,existingvalues(:,v)) * Unetflix(:,existingvalues(:,v))');
"""