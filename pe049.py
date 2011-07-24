#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe049.py - Project Euler
#
from math import sqrt

# 探索リスト
proposition_list = [],
# 素数リスト
prime_list = []

def initPrimeList(number):
	global prime_list, proposition_list
	
	proposition_list = range(2, number)
	# 素数リスト
	prime_list.append(proposition_list.pop(0))
	
	# エラトステネスの篩を使用する
	while max(proposition_list) >= pow(prime_list[-1], 2) :
		proposition_list =  [i for i in proposition_list if i % prime_list[-1]]
		prime_list.append(proposition_list.pop(0))

	prime_list = prime_list + proposition_list

initPrimeList(9999)

four_digit_prime_list = [i for i in prime_list if i > 1110 and (str(i)).find('0') == -1]
len_prime_list = len(four_digit_prime_list)

for i in xrange(len_prime_list):
	first_prime = four_digit_prime_list[i]
	for j in xrange(i+1, len_prime_list):
		second_prime = four_digit_prime_list[j]
		diff = second_prime - first_prime
		third_prime = second_prime + diff
		if sorted(list(str(first_prime))) != sorted(list(str(second_prime))):
			continue

		if third_prime in four_digit_prime_list and sorted(list(str(first_prime))) == sorted(list(str(third_prime))):
			print "(", first_prime, second_prime , third_prime, ")"
