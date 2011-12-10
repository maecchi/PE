#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe091.py - Project Euler
#
# 角POQ が直角になる数
# 角QPO が直角になる数
# 角OQP が直角になる数
# を求める
LIMIT_X = 50
LIMIT_Y = 50

def getSumOfRightAngle(tar_x,tar_y):
	count = 0
	for x in xrange(0, LIMIT_X+1):	
		for y in xrange(tar_y, LIMIT_Y+1):
			if tar_x == x and tar_y == y:
				continue
			if (tar_x*tar_x+tar_y*tar_y) - tar_x*x - tar_y*y == 0:
				count += 1
	return count

sum_of_POQ_right = LIMIT_X * LIMIT_Y

sum_of_QPO_right = 0
sum_of_OQP_right = 0

# 角QPOが直角になる数を求める
for x in xrange(1, LIMIT_X+1):
	for y in xrange(0, LIMIT_Y+1):
		if x == y == 0:
			continue
		sum_of_QPO_right += getSumOfRightAngle(x,y)

sum_of_OQP_right = sum_of_QPO_right

print sum_of_OQP_right + sum_of_QPO_right + sum_of_POQ_right

