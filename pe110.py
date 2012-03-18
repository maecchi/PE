#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe110.py - Project Euler
#
# 1/x + 1/y + 1/n を式変形すると
# (x-n)(y-n) = n^2
# このときn^2の約数の個数をNとすると
# xとyの組み合わせは(N+1)/2個存在する((x-n)=(y-n)=nの時以外入れ替え可能な点より)
# n^2の約数は素因数分解を用いて
# n = p1^e1*p2^e2*...*pn^enと表すことができるならば
# n^2 = p1^(2*e1)*p2^(2*e2)*...*pn^(2*en)なので
# 約数の個数は
# (2*e1+1)*....*(2*e2+1)と表すことができる
from itertools import *
from Queue import PriorityQueue
from math import sqrt

N = 4 * 10 ** 6
M = 2 * N - 1

# 初期タプルとnexts関数をもとに優先度キーの値を返却する
# init : 初期タプル
# nexts : 関数
# yieldで返る値 : (整数, (整数の素因数分解における指数値:左から順に2,3,5,7,11...))
def generateSorted(init, nexts):
	pq = PriorityQueue()
	pq.put(init)
	while not pq.empty():
		e = pq.get()
		yield e
		for e1 in nexts(e):
			pq.put(e1)

# 素数判定
def isPrime(n):
	# all(iterable):iterableの全ての要素が真ならTrueを返す
	return all(n % p != 0 for p in xrange(2,n))

# 素因数分解用素数列を生成
def generatePrimes(M):
	for p in (n for n in count(2) if isPrime(n)):
		yield p
		if M == 0:
			break
		M /= 3

# 次の数字および数字の素因数分解後の指数タプル列を返却する
# n : 対象数字
# es : 素因数分解における指数値のタプル列
def nexts((n, es)):
	# 素因数の指数列が一つしかない、または末尾の指数列の指数値が一つ前の指数値よりも小さい
	if len(es) == 1 or es[-1] < es[-2]:
		# 末尾の指数値を一つ増やす
		es1 = es[:-1] + (es[-1] + 1,)
		yield (n * primes[len(es)-1], es1)
	# 素数を一つ増やす
	es2 = es + (1,)
	yield (n * primes[len(es)], es2)

# 除数作成
def getNumDivisors(es):
	return reduce(lambda x,e: x * (e * 2 + 1), es, 1)

primes = list(generatePrimes(M))

print next((n, es) for n, es in generateSorted((2, (1,)), nexts) if getNumDivisors(es) > M)

