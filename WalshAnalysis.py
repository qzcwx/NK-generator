# Walsh Analysis Module
import numpy as np
def computeW(i,f):
    """ Walsh coefficient computation 

        This function receives a tuple of bit-string and a tuple of 
        corresponding function value, return the Walsh coefficient.
    """
    L = len(i[0])
    factor = (1.0 / len(f))
    return [ factor * subsum(i,i[j],f) for j in range(len(i)) ]

def subsum(i,j,f):
    """ compute the subsum for j bit-string """
    s = 0
    for index in range(len(i)):
       if bc(i[index],j)%2 == 0:
           s = s + f[index]
       else:
           s = s - f[index]
    return s

def bc(x,y):
    """ return the bit count of x and y """
    return bin( int(x,2) & int(y,2) ).count('1')
#    sum = 0;
#    for i in range(len(x)):
#        if x[i] == '1' and y[i] == '1':
#            sum = sum + 1
