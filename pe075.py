#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe075.py - Project Euler
#
# ピタゴラス数を使用する
# 3辺をa,b,cとするとき
# a = 2lmn, b = l(m^2 - n^2), c = l(m^2 + c^2)
# と表すことができる（m,nは整数 m > n, m+n は奇数, mとnは互いに素)
from fractions import gcd
from itertools import imap
from math import sqrt
LIMIT = 1500000
# ピタゴラス数を格納
method_list = [0] * (LIMIT+1)

def genPythagorasLength(N):
	for m in xrange(2, int(sqrt(N)) + 1):
		for n in xrange(m + 2 if m & 1 else m + 1, min(N / m + 1, m * 2), 2):
			if gcd(m, n) == 1:
				p = m * n
				for L in range(p, N/2, p): 
					yield L

for L in genPythagorasLength(LIMIT):
	method_list[L] += 1

print sum(imap(lambda x: method_list[x] == 1, xrange(LIMIT+1))) 
