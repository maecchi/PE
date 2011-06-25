#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe027.py - Project Euler
#

# number = n^2 + an + b
# n = 0
# number = b
# よってbは素数でないと題意が成り立たない
#
# n = 1
# number = a + (b+1)
# b+1はbが素数である以上偶数となるのでaは奇数である必要がある

max_a = 0
max_b = 0
max_prime_consecutive = 0

prime_list = set()
compos_list = set()

def init_prime_list(number):
	global prime_list

	for n in xrange(3, number, 2):
		is_not_prime = False
		for p in prime_list:
			if not n % p:
				is_not_prime = True
				break
		if not is_not_prime:
			prime_list.add(n)


def is_prime (number):
	global prime_list, compos_list		

	if number in prime_list:
		return True
	if number in compos_list:
		return False


	# 素数および合成数リストになかった場合
	for p in prime_list:
		if not number % p:
			compos_list.add(number)
			return False
	
	prime_list.add(number)
	return True

def getPrimeConsecutiveValue(a, b):
	number = 0
	
	while(1):
		if not is_prime(number*number+a*number+b):
			number -= 1
			break

		number += 1

	return number


init_prime_list(1000)
sort_prime_list = sorted(list(prime_list))
for b in sort_prime_list:
	for a in xrange(-999, 1000, 2):
		prime_consecutive = getPrimeConsecutiveValue(a, b)
		if prime_consecutive > max_prime_consecutive:
			max_a = a
			max_b = b
			max_prime_consecutive = prime_consecutive

print max_a, max_b, max_prime_consecutive
print max_a*max_b
