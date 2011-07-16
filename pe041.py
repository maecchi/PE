#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe041.py - Project Euler
#
from math import sqrt
# 1桁、4桁、7桁以外のPandigital数の桁の総和は３の倍数になるので３の倍数になる
# よって素数にはならない
SEVEN_LIMIT = 7654321
SEVEN_MIN = 1234567
FOUR_LIMIT = 4321
FOUR_MIN = 1234
seven_pandigital_strs = ['1', '2', '3', '4', '5', '6', '7']
four_pandigital_strs = ['1', '2', '3', '4', '5', '6', '7']
max_pandigital = 0
prime_set = set([2, 3, 5, 7])
compos_set = set([1, 4, 6, 8, 9, 10])

def isPrime (num):
	global prime_set, compos_set

	if num in prime_set:
		return True
	if num in compos_set:
		return False

	# 素数および合成数リストになかった場合
	for p in xrange(2, int(sqrt(num))+1):
		if not num % p:
			compos_set.add(num)
			return False

	prime_set.add(num)
	return True


for x in xrange(SEVEN_LIMIT, SEVEN_MIN-1, -1):
	str_num_list = sorted(list(str(x)))
	if str_num_list == seven_pandigital_strs:
		if (isPrime(x)):
			max_pandigital = x
			break

if max_pandigital == 0:
	for x in xrange(FOUR_LIMIT, FOUR_MIN-1, -1):
		str_num_list = sorted(list(str(x)))
		if str_num_list == four_pandigital_strs:
			if (isPrime(x)):
				max_pandigital = x
				break

print max_pandigital
	
