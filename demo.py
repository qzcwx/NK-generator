import WalshAnalysis as wal
import nkLandscape as nk
import AutoCorrelation as ac
import LocalOptima as lo
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

""" consider as a minimization problem """

def compFit(model):
    bitStr = []
    fit = []
    for i in range(int(math.pow(2,n))):
       bit = bin(i)
       bit = bit[2:]
       if len(bit) < n:
           bit = (n - len(bit))*'0' + bit
       bitStr.append(bit)
       fit.append(model.compFit(bitStr[i]))
    return bitStr, fit

random.seed(0)

n = 20
k = 9

print 'n', n, 'k', k

start = time.time()
w = np.zeros(math.pow(n,2))
print "t1", time.time() - start

start = time.time()
model = nk.NKLandscape(n,k)
print "t2", time.time() - start

start = time.time()
bitStr, fit = compFit(model)
print "t3", time.time() - start

start = time.time()
w = wal.computeW(bitStr, fit)
print "t4", time.time() - start

start = time.time()
autoCo = []
for i in range(n):
    autoCo.append(  ac.autoCorr(i, w) )
print "t5", time.time() - start

start = time.time()
numOpt = lo.localOpt(bitStr, fit)
print "t6", time.time() - start

#print 'bitStr', bitStr
#print 'fit', fit
#print 'ave of fit', sum(fit)/len(fit)
#print 'neigh', model.getNeigh()
#print 'w', w
print 'AutoCorrelation = ', autoCo
print 'Number of Local Optimum = ', numOpt

plt.title('Relationship between Auto-Correlation and $s$ ( n =' + str(n) + ', k =' + str(k) + ' )')
plt.xlabel('$s$')
plt.ylabel('$f(s)$')
plt.plot(range(n),autoCo,'o-')
plt.savefig('N'+str(n)+'K'+str(k)+'.eps')
