#!/usr/bin/pypy
# -*- coding: utf-8 -*-

from mathplus import timer, gcd, sqrt, isqrt

M = 120000

@timer
def pe(M):
    rad = [0] * M
    rad[1] = 1
    for p in range(2, M):
        if rad[p] > 0: continue
        isqrtp = isqrt(p)
        flag = True
        for q in range(2, isqrtp + 1):
            if p % q != 0: continue
            pp = p
            while pp % q == 0:
                pp //= q
            qq = q * rad[pp]
            pp = p
            while pp < M:
                rad[pp] = qq
                pp *= q
            flag = (q > isqrtp)
            break
        if flag:
            pp = p
            while pp < M:
                rad[pp] = p
                pp *= p

    s = 0
    for c in range(3, M):
        cc = (c-1)//rad[c]
        if rad[c-1] <= cc:
            s += c
        if cc < 6: continue
        if c % 2 == 0 and cc < 15: continue
        if c % 3 == 0 and cc < 10: continue
        for a in range(2, c//2):
            b = c - a
            if rad[a] > cc or rad[b] > cc: continue
            if rad[a] * rad[b] <= cc and gcd(a, b) == 1:
                s += c
    return s

print(pe(M))
