#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe115.py - Project Euler
#
# pe114で作成した関数を利用する

# 定数
M = 50
N = 50
LIMIT = 1000000

# while文初期値
n = N
count = 1

def getAnswer(m, n):
	if numbers[n] > 0:
		return numbers[n]
	if n <= 0:
		return 1
	
	numbers[n] =  sum([getAnswer(m, n-j-1) for i in xrange(0, n) for j in xrange(i+m, n+1)]) + 1
	
	return numbers[n] 


# 上限に達したらループを抜ける
while(count < LIMIT):
	n += 1
	# 途中で使用するf(N)を格納(nの値が増えるので都度初期化する)
	numbers = [-1] * (n+1)
	count = getAnswer(M, n)
	# f(N)の要素を初期化
	

print n
