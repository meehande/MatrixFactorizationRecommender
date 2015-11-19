# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:47:07 2015

@author: Deirdre Meehan
"""
import math 
import numpy

#A is the original matrix (R_matrix) - need to test it for zero elements
def rmse(A, B):
    # sqrt(sum(yn-y)^2)
    # element by element sum
     if(type(A) == numpy.ndarray):
         # 1. Element-wise subtraction on non-zero elements!
        C = A[A[:,:]!=0] - B[A[:,:]!=0]
        # 2. Square each element
        # 3. Sum of squares
        # 4. Square root of answer
        return math.sqrt(numpy.square(C).sum())

#TO DO: ENSURE IT ONLY LOOKS AT NON-ZERO ELEMENTS! DON'T WANT TO INCLUDE RECOMMENDATIONS
#TO DO: USE THIS FOR ITERATION CONTROL!
