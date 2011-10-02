#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe071.py - Project Euler
#
# [3/7 * n] / n  辺りに解があると予測する
from fractions import Fraction

LIMIT = 1000000
answer = 0
check_num = Fraction(3, 7)
check_list = []

# ユークリッド互除法による最大公約数を返す
def getHCFByEuclid(m, n):
	rest = m % n
	if rest == 0:
		return n
	else:
		return getHCFByEuclid(n, rest)


for n in xrange(1, LIMIT+1):
	frac =  Fraction(int(check_num * n), n)
	if frac < check_num and frac.numerator != 0 and getHCFByEuclid(frac.denominator, frac.numerator) == 1:
		check_list.append(frac)

print max(check_list)
