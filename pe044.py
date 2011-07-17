#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe044.py - Project Euler
#
# 対象の五角形を五角数の配列の中から大きい順に走査する
from math import sqrt

pentagon_list = []
answer = 0
x = 1

def isPentagonal(number):
	global pentagon_list

	if number in pentagon_list:
		return True

	x = (1 + sqrt(1+24 * number))/6
	return int(x) == x


while(answer == 0):
	pentagon = x * (3 * x - 1)/2
	
	for p in pentagon_list:
		diff = pentagon - p
		add = pentagon + p
		if isPentagonal(diff) and isPentagonal(add):
			answer = diff	
			break


	pentagon_list.insert(0,pentagon)
	x += 1

print answer
