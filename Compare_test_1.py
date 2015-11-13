# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:03:22 2015

@author: Deirdre Meehan
"""

import numpy
import time
# creating R with zeroes and using the basic method and the zero_matrix method 
# to see how long each takes with the same input for comparison


iterations = 5
n = 150
m = 300
d = 20
fraction_non_zero = 0.7

# correct matrix we want to get back to setup
U_matrix = numpy.random.rand(d, n)
V_matrix = numpy.random.rand(d, m)
R_matrix = numpy.dot(U_matrix.T, V_matrix)
#remobve values to zero
#find logical rep of R = R>0
R_temp = R_matrix > fraction_non_zero
for row in range(n):
    for col in range(m):
        if R_temp[row,col] == False:
            R_matrix[row,col] = 0.0
#use this to index columns
#benchmark against this (taking subset vs not)

# begin with random guesses of U, V
U_matrix = 5*numpy.random.rand(d, n)
V_matrix = 5*numpy.random.rand(d, m)


#set up matrices that will change
basic_u = U_matrix
basic_v = V_matrix
zero_u = U_matrix
zero_v = V_matrix

# BASIC MATRIX FACTORIZATION
t0 = time.time()
for i in range(iterations):
    for u in range (n): # u = row
        basic_u[:, u] = numpy.dot(numpy.dot(R_matrix[u, :], basic_v.T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(basic_v, basic_v.T))))

    for v in range(m): #for each row
        basic_v[:, v] = numpy.dot(numpy.dot(R_matrix[:, v].T, basic_u.T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(basic_u, basic_u.T))))

    basic_R = numpy.dot(basic_u.T, basic_v)
t1 = time.time()
basic_time = t1 - t0
# ZERO MATRIX FACTORIZATION

un,um = zero_u.shape
t0 = time.time()
for i in range(iterations):
    for u in range (n): # u = row
        zero_u[:, u] = numpy.dot(numpy.dot(R_matrix[u,R_matrix[u,:]!=0], zero_v[:,R_matrix[u,:]!=0].T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(zero_v[:,R_matrix[u,:]!=0], zero_v[:,R_matrix[u,:]!=0].T))))

    for v in range(m): #for each row
        zero_v[:, v] = numpy.dot(numpy.dot(R_matrix[R_matrix[:,v]!=0, v].T, zero_u[:, R_matrix[0:um,v]!=0].T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(zero_u[:, R_matrix[0:um,v]!=0], zero_u[:, R_matrix[0:um,v]!=0].T))))

    zero_R = numpy.dot(zero_u.T, zero_v)
t1 = time.time()
zero_time = t1 - t0

def compare_matrices(a, b, tolerance):
    if a.shape != b.shape:
        return "different dimensions"
    n, m = a.shape
    for row in range(n):
        for column in range(m):
            if a[row, column] != 0:
                if a[row, column] - b[row, column] > tolerance:
                    print "row: ", row, " column: ", column
                    print a[row, column], " & " ,b[row, column]
                    return False
    return True

print "Basic: ", compare_matrices(R_matrix, basic_R, 0.1)
print basic_time
print "Zero: ", compare_matrices(R_matrix, zero_R, 0.1)
print zero_time
























