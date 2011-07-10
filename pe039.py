#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe039.py - Project Euler
#

# a < b < c として考える
# 上記の仮定により題意に反するということはない

LIMIT = 1000
number_of_solutions = [0] * LIMIT

for a in xrange(1, LIMIT+1):
	for b in xrange(a+1, LIMIT+1):
		for c in xrange(b+1, LIMIT-a-b+1):
			if a + b < c:
				break
			if a**2 + b**2 == c**2:
				number_of_solutions[a+b+c-1] += 1
				break

print number_of_solutions.index(max(number_of_solutions)) + 1
