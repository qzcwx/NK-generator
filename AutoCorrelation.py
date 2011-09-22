# Compute Auto-Correlation with respect to Walsh coefficients w_i
import math

def autoCorr(s, w):
    allSolLen = len(w)
    n = int(math.log(allSolLen, 2))
    sum1 = 0
    sum2 = 0
    for i in [j for j in range(n) if j != 0]:
        sum1 = sum1 + lamd(i, n)**s * w[i]**2 
        sum2 = sum2 + w[i]**2 
    return sum1/sum2

def lamd(i, n):
    print 'i', i
    oneBit = bin(i)
    print 'str', oneBit
    oneBit = oneBit[2:]
    numOfOne = oneBit.count('1')
    print 'numOfOne', numOfOne
    return (1 -  2.0*numOfOne/n)
