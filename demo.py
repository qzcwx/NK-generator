import WalshAnalysis as wal
import nkLandscape as nk
import AutoCorrelation as ac
import numpy as np
import random

def compFit(model):
    bitStr = []
    fit = []
    for i in range(pow(2,n)):
       bit = bin(i)
       bit = bit[2:]
       if len(bit) < n:
           bit = (n - len(bit))*'0' + bit
       bitStr.append(bit)
       fit.append(model.compFit(bitStr[i]))
    return bitStr, fit

random.seed(0)

n = 5
k = 4

w = np.zeros(pow(n,k))
model = nk.NKLandscape(n,k)

bitStr, fit = compFit(model)

w = wal.computeW(bitStr, fit)

print 'bitStr', bitStr
print 'fit', fit
print 'ave of fit', sum(fit)/len(fit)
print 'neigh', model.getNeigh()
print 'w', w
print 'AutoCorrelation'
print ac.autoCorr(1, w)
