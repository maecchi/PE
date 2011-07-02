#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe032.py - Project Euler
#
# 「掛けられる数」*「掛ける数」= 「積」の３つの数字が９つの数字で表すには
# 1桁 * 4桁 = 4桁
# 2桁 * 3桁 = 4桁
# の２通りしか存在しない

pandigital_strs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pandigital_list = []

def findPandigital(a, b):
	global pandigital_list
	product = a * b
	digit_strs = (list(str(product)) + list(str(a)) + list(str(b)))
	if sorted(digit_strs) == pandigital_strs:
		if not product in pandigital_list:
			pandigital_list.append(product)

for x in xrange(1, 10):
	for y in xrange(1234, 9877):
		findPandigital(x,y)

for x in xrange(12, 99):
	for y in xrange(123, 988):
		findPandigital(x,y)

print sum(pandigital_list)
