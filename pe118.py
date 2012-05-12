#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe118.py - Project Euler
#
from itertools import *

# 素数リスト作成
def makeSieve(max_n):
    a = [ True ] * (max_n + 1)
    for p in (n for n in xrange(2, max_n + 1) if a[n]):
        for k in xrange(p * 2, max_n + 1, p):
            a[k] = False
    return [ n for n in xrange(2, max_n + 1) if a[n] ]

# 素数判定
def isPrime(n):
    return n >= 2 and all(n % p != 0 for p in
                takewhile(lambda p: p * p <= n, primes))

# 数字配列から数字を作成
def toNumber(a):
    return reduce(lambda x, y: x * 10 + y, a)

# 再帰で数字列を作成
def generatePart(a, k = 0):
	if k == len(a):
		yield (), ()
	else:
		for b, c in generatePart(a, k + 1):
			yield a[k:k+1] + b , c
			yield b, a[k:k+1] + c

# 数字要素タプルを2つのタプルに分解する
def generatePartitions(a, head):
    for b, c in generatePart(a[1:]):
        if not head or len(c) != 0:
            yield a[:1] + b, c

# 対象タプルから生成できる素数の数を返す
def numPrimes(a):
    return sum(imap(isPrime, imap(toNumber, permutations(a))))

# 素数の数を返す
def sumPrimesSet(a, head = True):
	def mul(b, c):
		if len(b) <= len(c):
			n = numPrimes(b)
			# 素数の数がないときは0を返す
			return n * sumPrimesSet(c, False) if n > 0 else 0
		else:
			n = sumPrimesSet(c, False)
			return numPrimes(b) * n if n > 0 else 0
	
	if len(a) == 0:
		return 1
	
	return sum(mul(b, c) for b, c in generatePartitions(a, head))

primes = makeSieve(10000)
print sumPrimesSet(tuple(range(1, 10)))
