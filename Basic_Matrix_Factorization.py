import random
import numpy
#correct matrix we want to get back to
R_matrix = numpy.matrix('1,2,;3,5')


R_tilde = numpy.matrix('0,0 ; 0,0')
iterations = 1000
sigma_rat = 0
rank = 2
n = 2
m = 2
d = 2
sigma = 0

#begin with random guesses of what could give R
U_matrix = numpy.random.random_integers(1, 6, (2, 2))

V_matrix = numpy.random.random_integers(1, 6, (2, 2))

for i in range (iterations):
    U_matrix = numpy.linalg.solve(numpy.dot(V_matrix,V_matrix.T)+ sigma_rat*numpy.eye(2), numpy.dot(V_matrix, R_matrix.T)).T

    V_matrix = numpy.linalg.solve(numpy.dot(U_matrix.T,U_matrix)+ sigma_rat*numpy.eye(2), numpy.dot(U_matrix.T, R_matrix))

    R_tilde = numpy.dot(U_matrix, V_matrix)

    print i
    print R_tilde

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