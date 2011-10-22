#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe080.py - Project Euler
#
# 2分探索で解を求める
# n < 100の時
# k <= 10^99 sqrt(n) < k+1
# k^2 <= n * 10^198 < (k+1)^2
# を満たす整数kが最初の100桁に相当する

from math import sqrt
answer = 0

for n in xrange(2, 100):
	if not sqrt(n) % 1:
		continue

	# 2分探索
	i = n * 10 ** 198
	l = 10**99
	r = (n+1) * 10 ** 99

	while r - l > 1:
		t = (r+l) / 2
		if (t**2 - i > 0):
			r = t
		else :
			l = t

	# 桁の和をとる
	answer +=  sum(map(lambda x: int(x), list(str(l))[:100]))

print answer
