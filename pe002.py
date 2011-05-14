# !/usr/bin/env python
# -*- coding : utf-8 -*-
#
# pe002.py - Project Euler
#

start_num = 1
next_num = 2
total = 0

while next_num < 4000000:
	tmp = next_num
	if not next_num % 2:
		total += next_num

	next_num += start_num
	start_num = tmp

print total
