#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe099.py - Project Euler
#
# 比較する数を小さくする
# a^b = c, d^e = f, c > fとするとき
# b*log(a) = log(c)という等式が成り立つので
# b*log(a) > d*log(e)という比較演算が成り立つ

from math import log10

# テキスト読み込み
n = 0
answer = 0
max_num = 0
for line in open('base_exp.txt', 'r'):
	n += 1
	# 要素一つ目：基底数、要素２つ目：指数
	num_list = map(lambda x: int(x), line.replace('\r\n', '').split(','))
	num = num_list[1] * log10(num_list[0])
	if max_num < num:
		max_num = num
		answer = n

print answer

