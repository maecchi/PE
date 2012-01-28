#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe100.py - Project Euler
#

# 青玉の数をB
# 玉の総数をTとすると
# B/T * (B-1)/(T-1) = 1/2
# 計算すると
# (2T-1)^2 - 2 (2B-1)^2 = -1
# X = 2T-1, Y = 2B-1とすると
# X^2 - 2*Y^2 = -1
# X = 2T-1, Y = 2B-1, D = 2 のペル方程式
# このときの最小解は(X,Y) = (1,1)

# このときの漸化式は
# X(i+1) = X(1)X(i) + D*Y(1)*Y(i)
# Y(i+1) = X(1)X(i) + Y(1)*Y(i)

MAX = pow(10,12)
init_x = 1
init_y = 1

total = 0
bule = 0

x,y = init_x, init_y

while(True):
	n = 0
	old_x = x
	old_y = y
	x = 1*old_x + 2*old_y
	y = 1*old_x + 1*old_y


	blue = (y+1)/2
	total = (x+1)/2

	# total が MAXを超えたら終了
	if total > MAX:
		break

print blue


