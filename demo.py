import WalshAnalysis as wal
import nkLandscape as nk
import numpy as np
import random

random.seed(0)

n = 5
k = 2

w = np.zeros(pow(n,k))
model = nk.NKLandscape(n,k)

bitStr = []
fit = []
for i in range(pow(2,n)):
   bit = bin(i)
   bit = bit[2:]
   if len(bit) < n:
       bit = (n - len(bit))*'0' + bit
   bitStr.append(bit)
   fit.append(model.compFit(bitStr[i]))

w = wal.computeW(bitStr, fit)
print 'bitStr', bitStr
print 'fit', fit
print 'ave of fit', sum(fit)/len(fit)
print 'neigh', model.getNeigh()
print 'w', w

# output
# [4.5, -0.5, 0.25, 1.25, 0.0, -0.5, 1.25, -1.25]
