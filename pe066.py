#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe066.py - Project Euler
#
from fractions import gcd
from math import sqrt

# ペル方程式の定理を使用する
LIMIT = 1000 
max_x = 0
max_D = 0

def intSqrt(num):
	return int(sqrt(num))

def generateCfractionCoeff(D):
	b,c,d = 0,1,1
	while True:
		a = (b + intSqrt(c * c * D)) / d
		yield a
		b -= a * d
		b,c,d = -b * d, c * d , c * c * D - b * b
		div = gcd(d, gcd(c,b))
		if div != 1:
			b,c,d = b / div, c / div, d / div

def isSatisfiedEquation(x, y, D):
	return x * x - y * y * D == 1

def initPellEqSolution(D):
	p1, q1, p2, q2 = 0 ,1 ,1, 0
	for a in generateCfractionCoeff(D):
		p2 , p1 = a * p2 + p1, p2
		q2 , q1 = a * q2 + q1, q2

		if isSatisfiedEquation(p2, q2, D):
			return p2, q2


for D in xrange(2, LIMIT+1):
	x,y = 0,0
	
	# 平方根が存在する数は除く
	if sqrt(D) % 1:
		x,y =  initPellEqSolution(D)
	
	if max_x < x:
		max_x = x
		max_D = D

print max_x, max_D
