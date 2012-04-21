#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe116.py - Project Euler
#

# 定数
N = 50
START_M = 2
END_M = 4
# 途中で使用するf(N)を格納

# 組み合わせ総数を求める
def getAnswer(m, l):
	numbers = [1] * m
	for n in range(m, l+1):
		numbers.append(numbers[n-m] + numbers[n-1])

	# 色のついたタイルを必ず含む必要があるので１減らす
	return numbers[n] - 1 

# 3 <= m <= 5までの組み合わせ総数の和を求める
print sum(getAnswer(m, N) for m in xrange(START_M, END_M+1))
