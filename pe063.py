#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe063.py - Project Euler
#

count = 0
digit = 1
while (1):
	is_count = False
	num = 1
	# num = 10 を超えると必ずn+1桁以上になる
	while (num < 10):
		target = num ** digit
		if len(str(target)) == digit:
			count += 1
			is_count = True
		elif len(str(target)) > digit:
			break

		num += 1

	if not is_count:
		break
	digit += 1

print count
