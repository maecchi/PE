#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe009.py - Project Euler
#
# Condition
# a + b + c = 1000
# a < b < c
product = 1

# 3a < a + b + c = 1000 -> a < 333
# ピタゴラスの定理を満たすためには三角形である必要がある 
# -> a + b > c = 1000 - a - b -> a + b > 500

for a in range(333, 0, -1):
	b_max_range = 1000 - a
	b_small_range = 500 - a
	if a > b_max_range:
		continue

	for b in range(b_max_range, b_small_range , -1):
		c = 1000 - a - b
		if (pow(a, 2) + pow(b, 2) == pow(c, 2)):
			product = a * b * c
			break

print product
