#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe094.py - Project Euler
#
# ペル方程式を使う
# ヘロンの公式より2辺をa, 残りをbとすると
# S = 1/2 * b * sqrt(a^2 - b^2/4)
# よってbは偶数
# b = 2n(nは整数)とするとa = 2n+1, 2n-1
# ∴  S = n * sqrt(3n^2± 4n+1)

# k^2 = 3n^2± 4n+1
# (3n± 2)^2 - 3k^2 = 1
# よってこれは
# x = (3n± 2) ,y = k, D = 3 のペル方程式
# このときの最小解は(x,y) = (2,1)

# ほかの全ての解は以下の式から求められる
# x(i) + y(i)*sqrt(3) = (2+sqrt(3))^i
# このときの漸化式は
# x(i+1) = 2x(i) + 3y(i)
# y(i+1) = x(i) + 2y(i)

# 周辺の長さは2a+b = 6n± 2
# x(i)で表すとx=3n+2(3で割ったとき２余るとき) 2x(i) - 2 (2x(i) - 6は考慮しない) 
# x=3n-2(3で割ったとき1余るとき) 2x(i) + 2 (2x(i) + 6は考慮しない) 



MAX = 1000000000
answer = 0
init_x = 2
init_y = 1

x,y = init_x, init_y
while(True):
	s = 0
	old_x = x
	old_y = y
	x = 2*old_x + 3*old_y
	y = old_x + 2*old_y

	if x % 3 == 2:
		s = 2*x - 2
	elif x %3 == 1:
		s = 2*x + 2

	# 面積が制限値以上になったら終了
	if s >= MAX:
		break
	answer += s

print answer
