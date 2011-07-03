#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe035.py - Project Euler
#
# 101以上の巡回素数について
# 各桁の数字は1,3,7,9の４通りのみ
# 2,4,5,6,8の数は1の位に数が巡回してきたとき割り切れてしまうため

LIMIT = 1000000
circular_primes = set([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])
use_numbers = [1, 3, 7, 9]
compos_list = set()

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

def isCircularPrime(num):
	global use_numbers, circular_primes, prime_list
	add_circular_primes = set()

	digits = list(str(num))
	digits.reverse()
	digits = map(lambda x: int(x), digits)

	if (num in circular_primes):
		return False


	for i in xrange(len(digits)):
		target_num =  sum([pow(10,x) * digits[x] for x in xrange(len(digits))])
		if not target_num in set_prime_list:
			return False

		add_circular_primes.add(target_num)
		pop_num = digits.pop()
		digits.insert(0, pop_num)

	circular_primes = circular_primes.union(add_circular_primes)
	return True

initPrimeList(LIMIT)
set_prime_list = set(prime_list)

for i in prime_list:
	isCircularPrime(i)

print len(circular_primes)
