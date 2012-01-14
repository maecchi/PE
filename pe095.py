#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe095.py - Project Euler
#

from itertools import ifilter, izip
from math import sqrt

def setPrimePowSum(n, p):
	s = 1
	while n % p == 0:
		s = s*p + 1
		n /= p
	return s, n


MAX = 1000000
# 約数の総和を値とした要素配列を作成する
# ただし最大数/2以上の約数は含まれない
def calcSumDivisors(max_n):
	a = range(max_n + 1)
	b = [1] * (max_n + 1)
	for p in ifilter(lambda p: a[p] == p, xrange(2, int(max_n/2) + 1)):
		# 約数の和を配列に格納していく
		for n in xrange(p+p, max_n + 1, p):
			b[n] += p

	return b

# 友愛鎖の長さを調べる
def calcLoopLength(num):
	global loop_list
	# 友愛数でないことが確定している
	if loop_list[num] > 0:
		return
	
	c = [num]
	s = set(c)
	
	while True:
		p = c[-1]
		q = sum_divisors_list[p]

		if q > MAX: # 範囲外
			for m in c:
				loop_list[m] = 0
			return
		elif q == num: # 友愛鎖確定
			for m in c:
				loop_list[m] = len(c)
			return
		elif loop_list[q] >= 0: # 1 to or branch(途中から友愛鎖になるまたは0)
			for m in c:
				loop_list[m] = 0
			return
		elif q in s: # 新しい鎖を作る
			k = c.index(q)
			for m in (c[i] for i in xrange(k)):
				loop_list[m] = 0
			for m in (c[i] for i in xrange(k, len(c))):
				loop_list[m] = len(c) - k
			return

		c.append(q)
		s.add(q)
			
def longer(x,y):
	return x if x[1] >= y[1] else y


sum_divisors_list = calcSumDivisors(MAX)
loop_list = [-1] * (MAX + 1)
loop_list[1] = 0

for n in xrange(2, MAX+1):
	calcLoopLength(n)

# izip()で0の値の配列を削除,reduce(longer)で最大の鎖の長さの組み合わせを表示
print reduce(longer, izip(xrange(MAX+1), loop_list))
