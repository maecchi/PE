#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe057.py - Project Euler
#
# n > 1 のとき
# a(n) = 1 + 1 / (2 + a(n-1))
# が成り立つ

from fractions import Fraction
LIMIT = 1000
count = 0

fraction_list = [0] * 1000
fraction_list[0] = Fraction(3,2)

for n in xrange(1, LIMIT):
	number = 1 + (1 / (1 + fraction_list[n-1]))
	fraction_list[n] = number
	
	if len(str(number.numerator)) > len(str(number.denominator)):
		count += 1

print count
