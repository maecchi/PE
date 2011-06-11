#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe023.py - Project Euler
#
limit_number = 28123
two_abundant_list = []
# 約数の総和が含まれた要素配列を生成する
array_sum_of_divisors = [0] * limit_number

for i in range(1, limit_number/2 + 1):
	for j in xrange(2 * i, limit_number + 1, i):
		array_sum_of_divisors[j-1] += i

abundant_number_list = set([i+1 for i in xrange(len(array_sum_of_divisors)) if i+1 < array_sum_of_divisors[i]])

# any() 内の式は２つの過剰数の和で表すことができる数字を判定する式
print sum([x for x in xrange(1,limit_number+1) if x < 24 or not any(x > a and (x-a) in abundant_number_list for a in abundant_number_list)])
	
