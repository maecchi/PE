#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe012.py - Project Euler
#

# 対称の約数の総数を求める関数
def getDivisors (number):
	divisors = {}
	divisor = 2
	sum_of_divisors = 0

	while number > 1 :
		count = 0
		while not number % divisor:
			number = number / divisor
			count += 1
		if count > 0:
			divisors[divisor] = count

		divisor += 1
	
	if len(divisors.values()) > 0:
		sum_of_divisors = reduce(lambda x, y : x * y, map((lambda x: x+1), divisors.values()))
	return sum_of_divisors


number = 1
triangle_number = 0
limit_sum_of_divisors = 500
while (1):
	triangle_number += number
	
	# 三角数の約数が規定数を超えたらwhileから抜けたす
	if getDivisors(triangle_number) > limit_sum_of_divisors:
		break;
	
	number += 1

print triangle_number
