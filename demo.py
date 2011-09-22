import WalshAnalysis as wal
import nkLandscape as nk
import AutoCorrelation as ac
import LocalOptima as lo
import numpy as np
import random
import time

""" consider as a minimization problem """

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

n = 10
k = 8

print 'n', n, 'k', k

start = time.time()
w = np.zeros(pow(n,k))
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

#print 'bitStr', bitStr
#print 'fit', fit
#print 'ave of fit', sum(fit)/len(fit)
#print 'neigh', model.getNeigh()
#print 'w', w

start = time.time()
autoCo = ac.autoCorr(1, w)
print "t5", time.time() - start

start = time.time()
numOpt = lo.localOpt(bitStr, fit)
print "t6", time.time() - start

print 'AutoCorrelation = ', autoCo
print 'Number of Local Optimum = ', numOpt
