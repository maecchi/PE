#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe065.py - Project Euler
#
# 連分数がp(n)/q(n) = [a(0): a(1), a(2)...a(n)]と表すことができるとき
# p(0) = a(0), q(0) = 1
# p(1) = a(0) * a(1) + 1, q(1) = a(1)
# n >= 2 のとき
# p(n) = a(n-1) * p(n-1) + p(n-2)
# q(n) = a(n-1) * q(n-1) + q(n-2)
# が成り立つ

from fractions import Fraction
LIMIT = 100

constant_list = [1] * (LIMIT+1)
convergent_list = [0] * LIMIT
for i in xrange(LIMIT / 3):
	constant_list[i * 3 + 2] = (i+1) * 2

constant_list[0] = 2

# 連分数の初期値を入れる
first_convergent = Fraction(2,1)
convergent_list [0] = first_convergent
convergent_list [1] = Fraction(constant_list[0]*constant_list[1]+1, constant_list[1])
# 連分数の計算
for n in xrange(2, LIMIT):
	before_conv = convergent_list[n-1]
	two_before_conv = convergent_list[n-2]
	convergent_list[n] = Fraction(
		constant_list[n] * before_conv.numerator + two_before_conv.numerator,
		constant_list[n] * before_conv.denominator + two_before_conv.denominator,
	)
	

# 解を求める
print sum(map(lambda x: int(x), list(str(convergent_list[n].numerator))))
