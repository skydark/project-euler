#!/usr/bin/python
# -*- coding: utf-8 -*-

#The smallest positive integer n for which the numbers n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

#What is the sum of all such integers n below 150 million?

#Answer:
	#676333270

from time import time; t=time()
from mathplus import get_primes_by_sieve, chain

M = 150000000#1000000
PM = M
dp = (1, 3, 7, 9, 13, 27)
ndp = (19, 21)
test = [10, 80, 130, 200]
circle = 210
P, _ = get_primes_by_sieve(PM)
testset = P[4:50]#(11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97)
#print time()-t

def is_prime2(n):
    for p in P:
        if p > n: break
        n2 = (n % p)**2
        for d in dp:
            if (n2+d) % p == 0: return False
    n2 = n*n
    for d in ndp:
        nn = n2+d
        flag = False
        for p in chain((3,7), testset, P):
            if p > n: break # <FIXME> nn = 10**2+21
            if nn % p == 0:
                flag = True
                break
        if not flag: return False
    return True

s = 0
flag = False
for p in testset:
    #print p, time()-t
    if not flag:
        if circle >= M:
            for j in range(len(test)-1, -1, -1):
                if test[j] < M: break
            test = test[:j+1]
            flag = True
        else:
            test = [u*circle+v for u in range(p) for v in test]
            circle *= p
    def test_prime(n):
        n2 = n*n
        for d in dp:
            if (n2 + d) % p == 0: return False
        return True
    test = list(filter(test_prime, test))
P = P[4+len(testset):]
#print time()-t, len(test)
s += 10 # <FIXME> 10 is missing
for n in test:
    if is_prime2(n):
        print(n)
        s += n

'''
for bn in range(0, M, 210):
    if bn % 1500000 == 0: print bn / 1500000
    for dn in (10, 80, 130, 200):
        n = bn + dn
        if n >= M: break
        if is_prime2(n):
            s += n
'''
print(s)#, time()-t
