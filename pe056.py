#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe056.py - Project Euler
#

LIMIT = 100
max_sum_of_digits = 0

for a in xrange(1, LIMIT+1):
	if not a % 10 :
		continue
	for b in xrange(1, LIMIT+1):
		digits_list = map(lambda x: int(x), list(str(a ** b)))
		sum_of_digits = sum(digits_list)
		if sum_of_digits > max_sum_of_digits:
			max_sum_of_digits = sum_of_digits

print max_sum_of_digits
