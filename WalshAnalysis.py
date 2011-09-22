# Walsh Analysis Module
def computeW(i,f):
    """ Walsh coefficient computation 

        This function receives a tuple of bit-string and a tuple of 
        corresponding function value, return the Walsh coefficient.
    """
    assert(len(i)>0 and len(i) == len(f)), 'length of bit-string is less than 1'
    L = len(i[0])
    return [ (1 / (2.0**L)) * subsum(i,i[j],f) for j in range(len(i)) ]

def subsum(i,j,f):
    """ compute the subsum for j bit-string """
    s = 0
    for index in range(len(i)):
        s = s + f[index] * (-1) ** bc(i[index],j)
    return s

def bc(x,y):
    """ return the bit count of x and y """
    sum = 0;
    for i in range(len(x)):
        sum = sum + int( x[i] ) * int( y[i] )
    return sum
