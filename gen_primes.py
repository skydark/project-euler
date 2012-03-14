#!/usr/bin/python
# -*- coding: utf-8 -*-

M = 100000000
def _get_prime_file(M, odd_only=False):
    return 'odd-primes-%s.txt' %M if odd_only else 'primes-%s.txt' %M

def gen_primes(M=M, odd_only=False):
    from mathplus import sieve
    sieves = sieve(M)
    if odd_only:
        primes = [str(i) for i, f in enumerate(sieves) if f and i != 2]
    else:
        primes = [str(i) for i, f in enumerate(sieves) if f]
    
    f = open(_get_prime_file(M, odd_only), 'w')
    f.write(','.join(primes))
    f.close()

def get_primes(M=M, odd_only=False):
    primes = [int(s) for s in open(_get_prime_file(M, odd_only)).read().split(',')]
    return primes

if __name__=='__main__':
    pass
    #gen_primes(10000000, odd_only=True)
