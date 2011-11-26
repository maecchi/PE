#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe088.py - Project Euler
#
from itertools import count, imap, ifilter, takewhile

LIMIT = 12000
prime_list = [2]

def head(a):
	for e in a:
		return e

def generateSumProduct(begin, end, s = 0, p = 1, limit = 2):
	for n in xrange(limit, end):
		if s:
			yield s + n - 1, p * n
		for s1, p1 in generateSumProduct((begin-1)/n + 1, (end-1)/n + 1, s + n - 1, p * n, n):
			yield s1, p1

def calcK(num):
	def is_full():
		return all(a[k] != 0 for k in xrange(num, 1, -1))
		
	a = [0] * (num + 1)

	begin,end = 1, 2

	# 定義した個数まで最小積和数を計算
	while not is_full():
		for s,n in generateSumProduct(begin, end):
			k = n - s
			# 最小値比較
			if k <= num and (a[k] == 0 or a[k] > n):
				a[k] = n
		begin, end = end, end*2
	
	return a

print sum(set(calcK(LIMIT)))
