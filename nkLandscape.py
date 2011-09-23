# generate NK-landscapes instances
## the encoding is in right to left fashion
## 00-0, 01-1, 10-2, 11-3 
import WalshAnalysis as wal
import random
import numpy as np
import matplotlib.pyplot as plt
import math

class NKLandscape:
    """ NK-landscape class """
    def __init__(self,inN,inK):
       self.n = inN
       self.k = inK
       self.genNeigh()
       self.genFunc()
       self.Kbits = genSeqBits(self.k+1)
    def dispNK(self):
        print self.n, self.k
    """ generate neighborhood """
    def genNeigh(self):
        self.neighs = []
        for i in range(self.n):
            oneNeigh = random.sample(range(self.n), self.k)
            while i in oneNeigh:
                oneNeigh = random.sample(range(self.n), self.k)
            self.neighs.append(oneNeigh)
#        print 'neighs', self.neighs
    def getNeigh(self):
        return self.neighs
    """ generate function value """
    def genFunc(self):
        self.func = []
        for i in range(self.n):
            oneFunc = []
            for j in range(int(math.pow(2,self.k+1))):
                oneFunc.append(random.random())
            self.func.append(oneFunc)
#        print 'func', self.func
    def getFunc(self):
        return self.func
    def getN(self):
        return self.n
    def genK(self):
        return self.k
    """ compute the fitness value"""
    def compFit(self, bitStr): 
        sum = 0
        for i in range(self.n):
            """ compose interacting bits """
            interBit = self.neighs[i][:]
            interBit.append(i)
            interBit.sort()
            """ extract corresponding bits """
            bits = [ bitStr[j] for j in interBit ]
            interStr = ''.join(bits)
            """ sum up the sub-function values """ 
            #print 'i', i, 'index in func', int(interStr,2), 'interStr', interStr
            sum = sum + self.func[i][int(interStr,2)]
        return sum
    def WalCof(self):
        """ compute the Walsh coefficients """
        subW = [] # subW is a N*2^K matrix
        for i in range(self.n):
            """ 1. Compute coefficients for each sub-functions """
            subWone = wal.computeW(self.Kbits, self.func[i])
            subW.append(subWone)
        w = np.zeros(math.pow(2,self.n))
        for i in range(int(math.pow(2,self.n))): # for every candidate solution
            iStr = bin(i)
            iStr = iStr[2:]
            if len(iStr) < self.n:
                iStr = (self.n - len(iStr))*'0' + iStr
            for j in range(self.n): # for every sub-function
                maskJ = self.neighs[j][:]
                maskJ.append(j)
                maskJ.sort()
                # pack iStr to a (k+1) length one
                maskStr = [iStr[k] for k in maskJ]
                maskStr = ''.join(maskStr)
                occurOneBit = self.indexOneBit(iStr)
                if self.checkInclude(occurOneBit, maskJ) == True :
                    extractBit = maskStr
                    w[i] = w[i] + subW[j][int(extractBit, 2)]
        return w
    def WalCofLinear(self):
        """ compute the Walsh coefficients in a linear time """
        subW = [] # subW is a N*2^K matrix
        for i in range(self.n):
            """ 1. Compute coefficients for each sub-functions """
            subWone = wal.computeW(self.Kbits, self.func[i])
            subW.append(subWone)
#        print 'subW', subW
        w = np.zeros(math.pow(2,self.n))
        for i in range(self.n): # i: index of subfunction
            interBits = self.neighs[i][:]
            interBits.append(i)
            interBits.sort()
#            print 'interBits',interBits
            for j in range(int(math.pow(2, self.k+1))): # j: index of substrings
                indexW = self.composeFullStr(i, j, interBits, self.n)
                w[indexW] = w[indexW] + subW[i][j]
#                print 'i',i,'j', j, 'w', w
        return w

    def composeFullStr(self, i, j, interBits, n):
        subStr = bin(j)
        subStr = subStr[2:]
        if len(subStr) < self.k+1:
            subStr = '0'*(self.k+1-len(subStr)) + subStr
#        print 'subStr', subStr
        indexSubOneBit = self.indexOneBit(subStr)
#        print 'indexSubOneBit', indexSubOneBit 
        iStr = ['0']*n
        for k in range(len(indexSubOneBit)):
            iStr[interBits[indexSubOneBit[k]]] = subStr[indexSubOneBit[k]]
        iStr = ''.join(iStr)
#        print 'iStr', iStr
        return int(iStr, 2)

    def checkInclude(self, occurOneBit, mask):
        for i in range(len(occurOneBit)):
            if occurOneBit[i] not in mask:
                return False
        return True

    def indexOneBit(self, iStr):
        range1 = range(len(iStr))
        return [ i for i in range1 if iStr[i] == '1']
            
def genSeqBits(n):
    bitStr = []
    for i in range(int(math.pow(2,n))):
       bit = bin(i)
       bit = bit[2:]
       if len(bit) < n:
           bit = (n - len(bit))*'0' + bit
       bitStr.append(bit)
    return bitStr

#model = NKLandscape(5,2)
#print model.getNeigh()
#print model.getFunc()
#print model.compFit('10001001010101010100')
