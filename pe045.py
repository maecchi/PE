#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe045.py - Project Euler
#
from math import sqrt

triangle_list = []
pentagonal_list = []
hexagonal_list = []
START = 286
answer = 0

def isPentagonal(num):
	x = (1 + sqrt(1 + 24 * num)) / 6
	return int(x) == x

def isTriangle(num):
	x = (1 + sqrt(1 + 8 * num)) / 2
	return int(x) == x


number = START
while(1):
	hex = number * (2 * number - 1)

	if isPentagonal(hex) and isTriangle(hex):
		answer = hex
		break

	number += 1


print answer
