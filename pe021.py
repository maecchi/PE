#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe021.py - Project Euler
#

limit_number = 10000
amicable_numbers = []

# 約数の総和が含まれた要素配列を生成する
array_sum_of_divisors = [0] * limit_number

for i in range(1, limit_number/2 + 1):
	for j in xrange(2 * i, limit_number + 1, i):
		array_sum_of_divisors[j-1] += i
	

# 友愛数を配列に格納する
for x in range(1, limit_number+1):
	sum_of_divisors = array_sum_of_divisors[x-1]

	# 完全数は友愛数と見なされない
	if sum_of_divisors != x and sum_of_divisors <= limit_number:
		if array_sum_of_divisors[sum_of_divisors-1] == x:
			amicable_numbers.append(x)

print sum(amicable_numbers)
