#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe064.py - Project Euler
#
# 題意のa(n) = X(n), Y(n)を以下のように表す
# X(n) 
# Y(n) = p / (sprt(n) - q)
from math import sqrt

period_list = []
LIMIT = 10000

for num in xrange(1, LIMIT+1):
	loop_count = 1

	# period計算
	sqrt_num = (sqrt(float(num)))
	if not (sqrt_num % 1) :
		continue
	x_first = int(sqrt_num)
	p_first = 1
	q_first = x_first 

	# ループ処理
	x = int(sqrt_num)
	p = 1
	q = x
	while(1):
		x = int(float(p/(sqrt_num-q)))
		p = (num - q ** 2) / p
		q = x * p - q

		if (p_first == p) and (q_first == q):
			period_list.append(loop_count)
			break
		loop_count += 1

# 奇数の周期を持つ平方根を計算
print len([x for x in period_list if x % 2])

