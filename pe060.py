#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe060.py - Project Euler
#
from random import seed, randrange
import itertools
import math

LIMIT = 10000
answer = 'MISSING'
mot_prime_list = {}

# 探索リスト
proposition_list = [],
# 素数リスト
prime_list = []

def Miller_Rabin(n):
    if n % 2 == 0:
        return False
    
    def MR_core(d, a, s = 1):
        if s == 1:
            return MR_core(d >> 1, a, 2) == n
        elif s == 2:
            if d & 1:
                m = MR_core(d >> 1, a, 3)
                s = m * m % n * a % n
                return n if s == n - 1 or s == 1 else s
            else:
                m = MR_core(d >> 1, a, 2)
                if m == n:
                    return n
                else:
                    s = m * m % n
                    return n if s == n - 1 else s
        elif s == 3:
            if d == 0:
                return 1
            else:
                m = MR_core(d >> 1, a, 3)
                if d & 1:
                    return m * m % n * a % n
                else:
                    return m * m % n
    
    k = 3
    return all(MR_core(n - 1, randrange(2, n)) for i in range(k))

# ミラーラビン法でPrimeListを作ってみる
def initPrimeList(number):
	global prime_list, proposition_list
	
	for n in xrange(2, number+1):
		if Miller_Rabin(n):
			prime_list.append(n)

def checkConnectPrime(num1, num2):
	con_num1 = int(str(num1) + str(num2))
	con_num2 = int(str(num2) + str(num1))

	return  Miller_Rabin(con_num1) and Miller_Rabin(con_num2)

# 題意を満たす素数か確認する再帰関数
def findChain(prime_list, rest):
	global mot_prime_list, answer
	if len(rest) == 5:
		if answer == 'MISSING':
			answer = sum(rest)
		else:
			answer = min(sum(rest), answer)
		return True
	else:
		if len(prime_list) == 0:
			return False
		for p in prime_list:
			p_list = list(set(prime_list) & set(mot_prime_list[p]))
			findChain(p_list, rest + [p])
	return False

initPrimeList(LIMIT)

for num in prime_list:
	check_prime =  [x for x in prime_list if x < num]
	passed_prime = []

	if num != 2:
		for c_num in check_prime:
			if checkConnectPrime(num, c_num):
				passed_prime.append(c_num)
	
	mot_prime_list[num] = passed_prime

	# 条件を満たした素数が４つ以上のとき確認
	if len(passed_prime) >= 4:
		findChain(passed_prime, [num])
			

print answer
