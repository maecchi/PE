#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe053.py - Project Euler
#
import itertools
import math

LIMIT = 100
MAX_COMBINATION = 1000000
answer = 0

def calcCombination(n, r):
	return math.factorial(n) / (math.factorial(r) * (math.factorial(n-r)))

# 組み合わせの数をrを起点にrの値を増やして走査する
def upperCombination(n,r):
	combs = 0

	for x in xrange(r, n+1):
		if calcCombination(n, x) > MAX_COMBINATION:
			combs += 1
		else:
			break
	return combs

# 組み合わせの数をrを起点にrの値を減らして走査する(起点rの組み合わせはチェックしない)
def underCombination(n,r):
	combs = 0

	for x in xrange(r-1, 0, -1):
		if calcCombination(n, x) > MAX_COMBINATION:
			combs += 1
		else:
			break
	return combs

for n in xrange(1,LIMIT+1):
	r = n/2
	
	answer += upperCombination(n, r)
	answer += underCombination(n, r)

print answer
