#!/usr/bin/python
# -*- coding: utf-8 -*-

# Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), and (N,N).

# It can be shown that f(10000) = 36.

# What is the sum of all positive integers N ≤ 1011 such that f(N) = 420 ?

#Answer:
    #271204031455541309

from mathplus import timer, get_primes_by_sieve, isqrt


N = 10 ** 11


@timer
def pe233():
    # Unreadable... = =||| #FML
    primes, _ = get_primes_by_sieve(N//(5**3*13**2)+1, odd_only=True)
    p4k1 = []
    p4k3 = []
    for p in primes:
        if p % 4 == 1:
            p4k1.append(p)
        else:
            p4k3.append(p)
    len_c = N // (5**3*13**2*17) + 1
    choices = [False] * len_c
    choices[1] = True
    for p in p4k3:
        if p >= len_c: break
        choices[p] = True
    for i in range(3, len_c, 2):
        if choices[i]: continue
        l = isqrt(i)
        for p in primes:
            if p > l:
                break
            if i % p == 0:
                if p % 4 == 3:
                    choices[i] = choices[i//p]
                break
    for i in range(1, (len_c+1)//2):
        choices[i*2] = choices[i]
    cs = [0] * len_c
    ss = 0
    for i, f in enumerate(choices):
        if f: ss += i
        cs[i] = ss
    s = 0
    Ndd = N // (5*5*13)
    Nd5 = N // 5
    for p1 in p4k1:
        k = p1 ** 3
        if k > Ndd: break
        for p2 in p4k1:
            if p2 == p1: continue
            k2 = k * p2 ** 2
            if k2 > Nd5: break
            for p3 in p4k1:
                if p3 == p1 or p3 == p2: continue
                k3 = k2 * p3
                if k3 > N: break
                s += k3 * cs[N//k3]
    for p1 in p4k1:
        k = p1 ** 7
        if k > Nd5: break
        for p2 in p4k1:
            if p2 == p1: continue
            k2 = k * p2**3
            if k2 > N: break
            s += k2 * cs[N//k2]
    for p1 in p4k1:
        k = p1 ** 10
        if k > Nd5: break
        for p2 in p4k1:
            if p2 == p1: continue
            k2 = k * p2**2
            if k2 > N: break
            s += k2 * cs[N//k2]
    return s

print(pe233())
