#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe001.py - Project Euler
#

total = 0

for num in range(1, 1000):
	if not num % (3 * 5): # 15の倍数
		total += num
	else:
		if not num % 3 or not num % 5: # 3または５の倍数
			total += num

print total
