import numpy

iterations = 5
sigma_rat = 0
rank = 2
n = 150
m = 300
d = 20
sigma = 0
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


# answer matrix
R_tilde = numpy.matrix('0,0 ; 0,0')

# begin with random guesses of U, V
U_matrix = 5*numpy.random.rand(d, n)
V_matrix = 5*numpy.random.rand(d, m)

#print "2nd U: \n", U_matrix
#print "2nd V: \n", V_matrix

un,um = U_matrix.shape
for i in range(iterations):
    for u in range (n): # u = row
        #try:
        U_matrix[:, u] = numpy.dot(numpy.dot(R_matrix[u,R_matrix[u,:]!=0], V_matrix[:,R_matrix[u,:]!=0].T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(V_matrix[:,R_matrix[u,:]!=0], V_matrix[:,R_matrix[u,:]!=0].T))))
        #except IndexError:
          #  pass
        # U_matrix = numpy.linalg.solve(numpy.dot(V_matrix,V_matrix.T)+ sigma_rat*numpy.eye(2), numpy.dot(V_matrix, R_matrix.T)).T
        # U_matrix[u,:] = numpy.linalg.solve(numpy.dot(V_matrix[:, u].T, V_matrix[:, u])+sigma_rat*numpy.eye(2), numpy.dot(V_matrix[u, :].T, R_matrix[u, :]))
        # IS Ruv A SCALAR??

    for v in range(m): #for each row
        # V_matrix = numpy.linalg.solve(numpy.dot(U_matrix.T,U_matrix)+ sigma_rat*numpy.eye(2), numpy.dot(U_matrix.T, R_matrix))
        # V_matrix[:,v] = numpy.linalg.solve(numpy.dot(U_matrix.T, U_matrix) + sigma_rat*numpy.eye(2), numpy.dot(U_matrix.T, R_matrix[:, v].T)).T
        V_matrix[:, v] = numpy.dot(numpy.dot(R_matrix[R_matrix[:,v]!=0, v].T, U_matrix[:, R_matrix[0:um,v]!=0].T), numpy.linalg.pinv(numpy.asmatrix(numpy.dot(U_matrix[:, R_matrix[0:um,v]!=0], U_matrix[:, R_matrix[0:um,v]!=0].T))))

    R_tilde = numpy.dot(U_matrix.T, V_matrix)

#print "ANSWER:\n", R_tilde


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

print compare_matrices(R_matrix, R_tilde, 0.1)

