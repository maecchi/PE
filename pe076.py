#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe076.py - Project Euler
#
# PE031と同様の考え方を行ってみる
LIMIT = 100
nums = [x for x in xrange(LIMIT, 0, -1)]

# 数の表し方の方法の数を格納する配列を作成
# way[i] に 数iに対する支払い方法の総数が入る(1つの正整数で表す手法もカウントされている)
ways = [1] + [0] * LIMIT

# 方法が限定される大きい数から走査を行う
for num in nums:
	for i in xrange(num, LIMIT+1):
		ways[i] += ways[i-num]

print ways[LIMIT] - 1
