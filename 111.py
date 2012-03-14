#!/usr/bin/python
# -*- coding: utf-8 -*-

#Considering 4-digit primes containing repeated digits it is clear that they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by 22, and so on. But there are nine 4-digit primes containing three ones:

#1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

#We shall say that M(n, d) represents the maximum number of repeated digits for an n-digit prime where d is the repeated digit, N(n, d) represents the number of such primes, and S(n, d) represents the sum of these primes.

#So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit prime where one is the repeated digit, there are N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = 22275. It turns out that for d = 0, it is only possible to have M(4, 0) = 2 repeated digits, but there are N(4, 0) = 13 such cases.

#In the same way we obtain the following results for 4-digit primes.
#Digit, d 	M(4, d) 	N(4, d) 	S(4, d)
#0 	2 	13 	67061
#1 	3 	9 	22275
#2 	3 	1 	2221
#3 	3 	12 	46214
#4 	3 	2 	8888
#5 	3 	1 	5557
#6 	3 	1 	6661
#7 	3 	9 	57863
#8 	3 	1 	8887
#9 	3 	7 	48073

#For d = 0 to 9, the sum of all S(4, d) is 273700.

#Find the sum of all S(10, d).

#Answer:
	#612407567715

from time import time; t=time()
from mathplus import get_primes_by_sieve, isqrt, product, permutations

M = 10
EM = 10**(M-1)
MM = isqrt(10**M)

primes, sieves = get_primes_by_sieve(MM)

def is_prime(n):
    if n < MM: return sieves[n]
    isqrtn = isqrt(n)
    for p in primes:
        if p > isqrtn: break
        if n % p == 0: return False
    return True

def gen(l, m, i):
    others = list(range(10))
    others.remove(i)
    past = set()
    ll = [True]*m+[False]*(l-m)
    for u in permutations(ll):
        if u in past: continue
        past.add(u)
        if u[-1] and i % 2 == 0: continue
        for v in product(*([others]*(l-m))):
            if not u[-1] and v[-1] % 2 == 0: continue
            n, k = 0, 0
            for j in u:
                n *= 10
                if j:
                    n += i
                else:
                    n += v[k]
                    k += 1
            yield n

def calc(l, d):
    for m in range(l+l%2-1, 0, -1):
        n = 0
        ret = set()
        for p in gen(l, m, d):
            if p >= EM and is_prime(p):
                n = 1
                ret.add(p)
        if n > 0:
            #print l, d, m, len(ret), sum(ret), ret
            return sum(ret)

print(sum(calc(M, d) for d in range(10)))#, time()-t
