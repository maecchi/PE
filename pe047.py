#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe047.py - Project Euler
#
from math import sqrt

LIMIT = 200000
SUM_OF_CONSECUTIVE_NUM = 4
# LIMITの値の中に題意を満たす数がなければMISSINGを返す
answer = 'MISSING'
# 探索リスト
proposition_list = [],
# 素数リスト
prime_list = []
# 素因数分解リスト
num_prime_factors_list = [[] for i in xrange(LIMIT)]

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

# 対象の値までの素因数分解リストを作成する
def setPrimeFactorToNum(LIMIT):
	global prime_list, num_prime_factors_list
	
	for prime in prime_list:
		for p in xrange(prime, LIMIT, prime):
			num_prime_factors_list[p-1].append(prime)
			
initPrimeList(LIMIT)
setPrimeFactorToNum(LIMIT)

for x in xrange(LIMIT-SUM_OF_CONSECUTIVE_NUM):
	target_len = len(num_prime_factors_list[x])
	if target_len == SUM_OF_CONSECUTIVE_NUM  and len(num_prime_factors_list[x+1]) == target_len and len(num_prime_factors_list[x+2]) == target_len and len(num_prime_factors_list[x+3]) == target_len:
		answer = x+1
		break

print answer
