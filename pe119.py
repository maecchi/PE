#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe119.py - Project Euler
#
# 先に題意を満たす整数を求める
# その後ソートして30番目の値を算出する
from math import *

LIMIT = 100
answer_list = []

# 各桁の総和を返す
def getSumOfDigit(num):
	return sum(map(lambda x: int(x), list(str(num))))


for i in xrange(2, LIMIT+1) :
	n = 2
	# 各桁の値を１にしても上限を超えてしまう時,whileを抜ける
	# (厳密にはi*10**nのときがあるが、下記の累乗計算では値が生成されない
	while i > int(log10(i**n)):
		val = i**n
		if i == getSumOfDigit(val):
			answer_list.append(val)	
		n += 1
if len(answer_list) >= 30:	
	print sorted(answer_list)[29]
else:
	print 'Not Found'
