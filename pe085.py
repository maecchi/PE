#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe085.py - Project Euler
#
# 横の長さがx,縦の長さが１yの長方形格子において
# 横の長さがm(1 <= m <= x), 縦の長さがn(1 <= n <= y)の長方形の格子は内部に
# ((x-m) + 1) * ((y-n) + 1)個存在する

from math import sqrt

# 上限(1x1の格子のみで解を満たしてしまう場合)
LIMIT_SIZE = 2 * 10 ** 6
LIMIT_LENGTH = int(sqrt(LIMIT_SIZE)) + 1
answer_distance = LIMIT_SIZE
answer = 1
end_flag = False

# 格子数の総和を算出する(公式使用..)
def getLatticeCount(x, y):
	return (x * (x+1) / 2) * (y * (y+1) / 2)

for x in xrange(1, LIMIT_LENGTH):
	is_change_answer = False
	for y in xrange(x+1, LIMIT_LENGTH):
		count = getLatticeCount(x,y)
		
		if (abs(LIMIT_SIZE - count) == 0 ):
			answer_distance = abs(LIMIT_SIZE - count)
			answer = x * y
			end_flag = True
			is_change_answer = True
			break
		elif (abs(LIMIT_SIZE - count) < answer_distance):
			answer_distance = abs(LIMIT_SIZE - count)
			answer = x * y 
			is_change_answer = True
		elif is_change_answer == True:
			break
		
	if end_flag == True:
		break

print answer
