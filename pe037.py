#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe037.py - Project Euler
#
from math import sqrt

prime_set = set([2, 3, 5, 7])
compos_set = set([1, 4, 6, 8, 9, 10])
check_num = 11
both_truncable_prime_list = []

def isPrime(num):
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

def leftDigitDeletePrimeCheck(num):
	global prime_set

	num_len = len(list(str(num)))
	num = num % pow(10, num_len - 1)

	while (num > 0):
		if not num in prime_set:
			return False
		num = num % pow(10, num_len - 1)
		num_len = len(list(str(num)))

	return True

def rightDigitDeletePrimeCheck(num):
	global prime_set

	num = int(num / 10)

	while (num > 0):
		if not num in prime_set:
			return False
		num = num / 10

	return True

while(len(both_truncable_prime_list) < 11):

	# 素数確認
	if isPrime(check_num):

		if check_num < 10:
			check_num += 1
			continue

		check_num_str = list(str(check_num))
		if ('4' in check_num_str) or ('6' in check_num_str) or ('8' in check_num_str) or ('0' in check_num_str):
			check_num += 1
			continue

		# 左から切り詰める
		# 右から切り詰める
		if leftDigitDeletePrimeCheck(check_num) and rightDigitDeletePrimeCheck(check_num):
			# どっちも通り抜けたものが題意を満たす素数
			both_truncable_prime_list.append(check_num)


	check_num += 1

print sum(both_truncable_prime_list)


