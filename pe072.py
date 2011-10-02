#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe072.py - Project Euler
#
# オイラーの関数φ(n)を1から10^6まで求めて総和を算出する
from fractions import Fraction
from itertools import ifilter, imap, takewhile
from math import sqrt

LIMIT = 1000000
answer = 0
prime_list = []

# エラストテネスの篩
def getPrimeList(max_n):
	# 奇数リスト作成
	L = (max_n + 1) / 2
	a = [ True ] * L
	for k in ifilter(lambda p: a[p], xrange(1, int(sqrt(max_n)) / 2 + 1)):
		# a[p] = Trueならfor分処理実行 
		p = k * 2 + 1
		for n in xrange(k * 3 + 1, L, p): #同一素数を持つものはFalse
			a[n] = False
	return [ 2 ] + map(lambda k: k * 2 + 1,ifilter(lambda k: a[k], xrange(1, L)))


def getPhi(n, k0=0):
	global prime_list,L
	yield 1
	for k in takewhile(lambda k:prime_list[k] <= n, xrange(k0, L)):
		p = prime_list[k]
		q = p
		rest = n

		while rest >= p:
			rest /= p
			for phi in getPhi(rest, k+1):
				yield q * (p-1) / p * phi
			q *= p
prime_list = getPrimeList(LIMIT) 
L = len(prime_list)

print sum(getPhi(LIMIT)) - 1 # 初回のyield分を引く
