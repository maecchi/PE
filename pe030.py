#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe030.py - Project Euler
#
#
# 9^5 = 59049より
# 5 * 9^5 = 295245 > 99999
# 6 * 9^5 = 354294 < 999999
# よって題意を満たす数の上限は354294

total = 0

for n in xrange(2, 354295):
	power_digits =  map(lambda x: pow(int(x),5) , list(str(n)))
	if sum(power_digits) == n:
		total += n
		
print total
