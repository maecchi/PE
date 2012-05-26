#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe122.py - Project Euler
#

from itertools import *

# Mの最大値を決定する
def calcMaxM(c, n):
	if n % 2 == 0:
		return c[n/2] + 1
	else:
		return c[n/2] + 2


N = 200
M = next(n for n in count() if 1 << n >= N)
a = [ [] for k in xrange(N + 1)]
a[1] = [ (1,)]
c = [0]

for n in xrange(1, N+1):
	c.append(min(len(x) - 1 for x in a[n]))
	max_m = calcMaxM(c, n)
	for x in a[n]:
		for m in x:
			n = m + x[-1]
			if n <= N and len(x) <= calcMaxM(c, n):
				a[n].append(x+(n,))

print sum(c[n] for n in xrange(1, N+1))
