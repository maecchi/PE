#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe070.py - Project Euler
#
# pe069同様オイラーの関数を使用する
# 互いに素な数φ(n)は
# φ(n) = n * Π(1-1/p(k))で表すことができる
# よって
# φ(n) / n = Π(1-1/p(k))
# p(k) は素数
# ゆえに素因数が多くなると値は小さくなるので
# n / φ(n) が最小となるnを求めるにはφ(n) / n が最大となるnを求めればよい
# 最小となるnは規定値において素因数が少なく、素因数の値が大きいものが解となる

from math import sqrt
from random import seed, randrange
LIMIT = 10 ** 7
answer = 'None'
min_n_per_phi = 100000
prime_list = [2]

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

def initPrimeList(num):
	global prime_list

	for n in xrange(2, num):
		if Miller_Rabin(n):
			prime_list.append(n)

def getPhiFromTwoPrime(p1, p2):
	return float(p1) * float(p2) * (float(1) - float(1)/p1) * (float(1) - float(1)/p2)


initPrimeList(int(sqrt(LIMIT)) + 2000)

for p1 in prime_list[::-1]:
	for p2 in prime_list[::-1]:
		if p1 * p2 > LIMIT:
			continue
		if p1 > p2:
			break

		target_num = p1 * p2
		phi_from_two_prime = int(getPhiFromTwoPrime(p1, p2))
		if sorted(list(str(target_num))) == sorted(list(str(phi_from_two_prime))):
			if float(target_num)/phi_from_two_prime < min_n_per_phi:
				min_n_per_phi = float(target_num)/phi_from_two_prime
				answer = target_num 
				break


print answer
