#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe034.py - Project Euler
#
# 9! = 362880より
# 6 * 9! = 2177280 > 999999
# 7 * 9! = 2540160 < 9999999
# よって題意を満たす数の上限は2540160

import math

LIMIT = 2540160
total = 0

def IsEqualFactorialDigits(num):
	digits = map(lambda x: int(x), list(str(num)))
	factorial_num = sum(map(lambda y: math.factorial(y), digits))

	if num == factorial_num:
		return True
	else:
		return False

for num in xrange(3, LIMIT+1):
	if IsEqualFactorialDigits(num):
		total += num

print total
