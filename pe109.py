#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe109.py - Project Euler
#
# ダブルの点数を除いた点数から取りうる全てのポイントを並べて前から取っていく

from itertools import *

NUM = 20
LIMIT = 100
total = 0

double_score_list = range(2, 2*(NUM+1), 2) + [50]
all_score_list = range(1, NUM+1) + [25] + double_score_list + range(3, 3*(NUM+1), 3)

# 残りの試行回数と使用したスコアリスト要素番号を引数として
# スコアを生成する
def generateScore(c, k0):
	if c == 1: # 最後の試行のとき
		for pt in double_score_list:
			yield pt
	else : # それ以外の試行回数のとき
		for k in xrange(k0, len(all_score_list)):
			pt0 = all_score_list[k]
			for pt in generateScore(c-1, k):
				yield pt + pt0

for c in range(1, 4):
	total +=  sum(1 for pt in ifilter(lambda x: x < LIMIT, generateScore(c, 0)))

print total
