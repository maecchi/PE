#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe081.py - Project Euler
#
# Project 18,67と同様の考え方を使用する
# 到達位置から始点に向かって最小の値の合計を置き換えていく(向きは左方向または上方向)

rows= []

for line in open('matrix.txt', 'r'):
	rows.append(map(lambda x: int(x), line.replace('\r\n', '').split(',')))

rows_key_max = len(rows) - 1

for i in xrange(rows_key_max, -1, -1):
	for j in xrange(rows_key_max, -1 ,-1):
		if (i == rows_key_max) and (j == rows_key_max): # 終点では何もしない
			continue

		if (j == rows_key_max):
			min_num = rows[i+1][j]
		elif (i == rows_key_max):
			min_num = rows[i][j+1]
		else:
			min_num = min(rows[i+1][j], rows[i][j+1])

		# 要素を最大値で書き換える
		rows[i][j] += min_num


print rows[0][0]

