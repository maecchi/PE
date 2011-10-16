#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe078.py - Project Euler
#
# pe076,pe077と異なり、計算量が多いためオイラーの五角数定理を使用する
p_dic = {}
number = 2

def P(n):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	
	if n in p_dic:
		return p_dic[n]
	
	k = 1
	count = 0

	while True:
		n1 = n - (3*k*k-k)/2
		n2 = n - (3*k*k+k)/2
		count += (-1)**(k+1)*(P(n1)+P(n2))

		if n2 <= 0:
			p_dic[n] = count
			return count
		k += 1

while True:
	if not P(number) % 1000000:
		break
	number += 1

print number
