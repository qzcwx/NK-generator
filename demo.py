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
    n = model.getN()
    fit = np.zeros(math.pow(2,n))
    bitStr = nk.genSeqBits(n)
    for i in range(int(math.pow(2,n))):
       fit[i] = model.compFit(bitStr[i])
    return bitStr, fit

random.seed(0)

#n = 15
#k = 4
for k in range(4,10):
    for n in [i for i in range(21) if i >= k+1 ]:
        print 'n', n, 'k', k

        #start = time.time()
        w = np.zeros(math.pow(n,2))
        #print "t1", time.time() - start

        #start = time.time()
        model = nk.NKLandscape(n,k)
        #print "t2", time.time() - start

        start = time.time()
        w0 = model.WalCof()
        print "t0", time.time() - start

        start = time.time()
        w00 = model.WalCofLinear()
        print "t00", time.time() - start

        #start = time.time()
        bitStr, fit = compFit(model)
        #print "t3", time.time() - start

        #start = time.time()
        #w = wal.computeW(bitStr, fit)
        #print "t4", time.time() - start

        #print 'w0', w0
        #print 'w', w
        #print 'difference', w0-w

        start = time.time()
        #autoCo = []
        #for i in range(n):
        #    autoCo.append(  ac.autoCorr(i, w0) )
        autoCo = ac.autoCorr(1, w0)
        print "t5", time.time() - start

        #start = time.time()
        #numOpt = lo.localOpt(bitStr, fit)
        #print "t6", time.time() - start

        #print 'bitStr', bitStr
        #print 'fit', fit
        #print 'ave of fit', sum(fit)/len(fit)
        #print 'neigh', model.getNeigh()
        #print 'w0', w0
        #print 'w00', w00
        print 'r(1) = ', autoCo
        #print 'Num of Local Optimum = ', numOpt

        #plt.title('Relationship between Auto-Correlation and $s$ ( n =' + str(n) + ', k =' + str(k) + ' )')
        #plt.xlabel('$s$')
        #plt.ylabel('$f(s)$')
        #plt.plot(range(n),autoCo,'o-')
        #plt.savefig('N'+str(n)+'K'+str(k)+'.eps')
        print '***********************************'
