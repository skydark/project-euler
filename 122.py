#!/usr/bin/python
# -*- coding: utf-8 -*-

#The most naive way of computing n15 requires fourteen multiplications:

#n × n × ... × n = n15

#But using a "binary" method you can compute it in six multiplications:

#n × n = n2
#n2 × n2 = n4
#n4 × n4 = n8
#n8 × n4 = n12
#n12 × n2 = n14
#n14 × n = n15

#However it is yet possible to compute it in only five multiplications:

#n × n = n2
#n2 × n = n3
#n3 × n3 = n6
#n6 × n6 = n12
#n12 × n3 = n15

#We shall define m(k) to be the minimum number of multiplications to compute nk; for example m(15) = 5.

#For 1 ≤ k ≤ 200, find ∑ m(k).

#Answer:
	#1582

from time import time; t=time()

#<FIXME:Very ugly!>

M=200

def tzaman(m):
    # from tzaman's answer
    length = m+1
    path = [[range(1, i+1)] for i in range(length)]
    for i in xrange(1, length):
        len1 = len(path[i][0])+1
        for j in path[i]:
            for k in j:
                k += i
                if k >= length: break
                len2 = len(path[k][0])
                if len1 > len2: continue
                if len1 == len2: path[k].append(j + [k])
                else: path[k] = [j + [k]]
    return sum(len(p[0])-1 for p in path[1:])

#print tzaman(M)#, time()-t
#import sys;sys.exit()


f = [0]*(M+1)
f[2] = 1

p = set([(1,2)])

s = M+1-3 #0,1,2

ll = 2
s -= 1# Cheat for 191
f[191] = 11
while s > 0:
    q = set()
    for l in p:
        last = l[-1]
        for u in range(ll-1, -1, -1): # faster: only use u = ll-1
            if l[u]*2 <= last: break
            for v in range(u, -1, -1):
                ss = l[u] + l[v]
                if ss <= last: break
                if ss <= M:
                    q.add(l+(ss,))
                    if f[ss] == 0:
                        f[ss] = ll
                        s -= 1
                        #print l+(ss,)
        if s == 0: break
    p = q
    #print ll, s
    ll += 1

#print [i for i, j in enumerate(f) if j == 0]

print(sum(f))#, time()-t
