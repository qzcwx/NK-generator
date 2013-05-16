# generate NK-landscapes instances
## the encoding is in right to left fashion
## 00-0, 01-1, 10-2, 11-3 
import random
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
        return sum/self.n
    
            
def genSeqBits(n):
    bitStr = []
    for i in range(int(math.pow(2,n))):
       bit = bin(i)
       bit = bit[2:]
       if len(bit) < n:
           bit = (n - len(bit))*'0' + bit
       bitStr.append(bit)
    return bitStr

# testing purpose
model = NKLandscape(5,2)
print model.getNeigh()
print model.getFunc()
print model.compFit('10001')
