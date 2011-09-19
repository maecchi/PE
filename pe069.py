#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe069.py - Project Euler
#
# オイラーの関数を使用する
# 互いに素な数φ(n)は
# φ(n) = n * Π(1-1/p(k))で表すことができる
# よって
# φ(n) / n = Π(1-1/p(k))
# p(k) は素数
# ゆえに素因数が多くなると値は小さくなるので
# n / φ(n) が最大となるnを求めるにはφ(n) / n が最小となるnを求めればよい
# 最小となるnは全て素因数で構成される数が最小のnとなる
from random import seed, randrange

LIMIT = 1000000
answer = 1
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

initPrimeList(1000)

for n in prime_list:
	if n * answer > LIMIT:
		break
	else:
		answer *= n

print answer
