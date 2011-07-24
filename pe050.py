#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe050.py - Project Euler
#
from math import sqrt
import itertools

LIMIT = 1000000
# 題意の値を見つけたかのフラグ
find_flag = False
# 探索リスト
proposition_list = [],
# 素数リスト
prime_list = []

# 素数リストの小さい順に値を加算して100万を超える前までの素数を格納した配列
under_million_prime_list = []

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

initPrimeList(LIMIT)

for p in prime_list:
	under_million_prime_list.append(p)
	if sum(under_million_prime_list) >= LIMIT:
		under_million_prime_list.pop()
		break
	
limit_digit_sum = len(under_million_prime_list)

# 100万を超える直前の素数群において使用していた個数を一つずつ少なくしていき、素数の値を形成できるか確認する
for count in xrange(limit_digit_sum-1, 0 ,-1):
	x = 0
	while sum(prime_list[x:count+x]) < LIMIT:
		if sum(prime_list[x:count+x]) in prime_list:
			find_flag = True
			print count, sum(prime_list[x:count+x])
			break
		x += 1
	if find_flag:
		break
	
