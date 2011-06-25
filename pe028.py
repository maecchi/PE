#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe028.py - Project Euler
#
#
# 題意を満たす条件において
# 最右側の対角線上の頂点の和と最左側の対角線上の頂点の和は等しい
# よって片側の対角線上の頂点の和を２倍した数に１を足せば題意を満たす値を求めることができる

sum = 1 # 中央の値を初期値とする

for n in xrange(3, 1002, 2):
	right_top_diagonals = pow(n,2)
	right_bottom_diagonals = pow(n,2) - 3 * (n-1)
	sum += 2 * (right_top_diagonals + right_bottom_diagonals)

print sum
