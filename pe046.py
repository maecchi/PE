#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe046.py - Project Euler
#
from math import sqrt

LIMIT = 10000
# LIMITの値の中に題意を満たす数がなければMISSINGを返す
answer = 'MISSING'
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
	while max(proposition_list) > pow(prime_list[-1], 2) :
		proposition_list =  [i for i in proposition_list if i % prime_list[-1]]
		prime_list.append(proposition_list.pop(0))

	prime_list = prime_list + proposition_list

initPrimeList(LIMIT)


for num in xrange(2, LIMIT + 1):
	is_answer_number = True

	if (num % 2) & (not num in prime_list):
		for d in xrange(1, int(sqrt(num))): 
			check_num = num - 2 * pow(d, 2)

			if check_num in prime_list:
				is_answer_number = False
				break

		if is_answer_number:
			answer = num
			break

print answer
