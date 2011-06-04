#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe018.py - Project Euler
#
triangle_elements = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

#
#   a   ->  A     
#  b c    
#
# 最小の三角形において頂点から下まで移動するときの数値の合計の最大値を求める
def getMaxOneTopNumber(top_number, b_left_num, b_right_num):
	return top_number + max(b_left_num, b_right_num)


# トップダウンで求めるのではなく、ボトムアップで最大値を求めていく
# 最大値の計算回数がΣ(n-1)回で終わらせることができる
for x in xrange(len(triangle_elements) -2 , -1, -1):
	row_elements = triangle_elements[x]
	comp_elements = triangle_elements[x+1]

	# 要素を最大値で書き換える
	for y in xrange(len(row_elements)):
		triangle_elements[x][y] =  getMaxOneTopNumber(row_elements[y], comp_elements[y], comp_elements[y+1])

print triangle_elements[0][0]
