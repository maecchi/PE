#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe033.py - Project Euler
#

from fractions import Fraction

fractions = 1

def is_non_trivial(x, y):

	# 10の倍数の場合は題意の自明な数に相当する
	if not x % 10 or not y % 10:
		return False;

	quotient = Fraction(x,y)

	x_digit = list(str(x))
	x_digit = map(lambda x: int(x), x_digit)
	y_digit = list(str(y))
	y_digit = map(lambda y: int(y), y_digit)

	if (x_digit[0] == y_digit[1]):
		if (Fraction(x_digit[1], y_digit[0]) == quotient):
			return True
	elif (x_digit[1] == y_digit[0]):
		if (Fraction(x_digit[0],y_digit[1]) == quotient):
			return True
	
	return False


for x in xrange(12, 100):
	for y in xrange(x+1, 100):
		if is_non_trivial(x, y):
			fractions *= Fraction(x,y)

print fractions.denominator

