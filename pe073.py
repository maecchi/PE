#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe073.py - Project Euler
#
from fractions import Fraction
import math

LIMIT = 12000
min_num = Fraction(1,3)
max_num = Fraction(1,2)
answer_list = []
counter = 0

# ユークリッド互除法による最大公約数を返す
def getHCFByEuclid(m, n):
	rest = m % n
	if rest == 0:
		return n
	else:
		return getHCFByEuclid(n, rest)

for n in xrange(2, LIMIT+1):
	min_numerator = int(math.ceil(float(n)/3))
	max_numerator = int(math.floor(float(n)/2))

	for m in xrange(min_numerator, max_numerator+1):
		if getHCFByEuclid(n,m) == 1:
			frac = Fraction(m,n)
			if frac > min_num and frac < max_num:
				counter += 1

print counter
