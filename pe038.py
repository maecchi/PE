#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe038.py - Project Euler
#

# 連結積のおいて連結する数はn > 1より2個以上
# よって整数の範囲は9999まで
max_pandigital = 0
pandigital_strs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for x in xrange(1, 10000):
	concatenated_number_str = ''
	for n in xrange(1, 10):
		num_str = str(n*x)
		concatenated_number_str += num_str
		
		if len(concatenated_number_str) > 10:
			break;
		elif sorted(list(concatenated_number_str)) == pandigital_strs:
			max_pandigital = max(max_pandigital, concatenated_number_str)
			break;

print max_pandigital
