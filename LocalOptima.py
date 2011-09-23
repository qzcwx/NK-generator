# this function counts the number of local optimum over the entire search space
import random
import numpy as np

def localOpt(bitStr, f):
    n = len(bitStr[0])
    num = 0
    compCount = 0
    loMark = []
    """ initialize all markers to true """
    for i in range(len(bitStr)):
        loMark.append(True)
    """ generate the random solution under consideration for local optimum """
    while loMark.count(True)>0:
        sol = ''
        for i in range(n):
            sol = sol + str(random.randint(0,1))
        while loMark[int(sol,2)] == False:
            sol = ''
            for i in range(n):
                sol = sol + str(random.randint(0,1))
#        print 'sol', sol
        """ consider all the neighborhoods """
        solIndex = int(sol, 2)
        for i in range(n):
            neigh = ''
            for j in range(n):
                if i == j:
                    neigh = neigh + flipBit(sol[j])
                else:
                    neigh = neigh + sol[j]
           # print 'neigh', neigh, 'i', i
            neighIndex = int(neigh, 2)
            compCount = compCount + 1
            if f[solIndex]>f[neighIndex]:
                loMark[solIndex] = False
                break
            else:
                loMark[neighIndex] = False
        if loMark[solIndex]==True:
            num = num + 1
            loMark[solIndex] = False
 #       print loMark
    print 'comp times', compCount
    return num

def flipBit(bit):
    if bit == '0':
        return '1'
    else:
        return '0'
