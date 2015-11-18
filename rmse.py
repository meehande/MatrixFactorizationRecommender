# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:47:07 2015

@author: Deirdre Meehan
"""
import math 
import numpy

def rmse(A, B):
    # sqrt(sum(yn-y)^2)
    # element by element sum
    
    # 1. Element-wise subtraction
    C = A - B
    # 2. Square each element
    numpy.square(C)
    # 3. Sum of squares
    # 4. Square root of answer
    return math.sqrt(C.sum())

#TO DO: ENSURE IT ONLY LOOKS AT NON-ZERO ELEMENTS! DON'T WANT TO INCLUDE RECOMMENDATIONS
#TO DO: USE THIS FOR ITERATION CONTROL!
