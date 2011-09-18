#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe067.py - Project Euler
#
# pe017.pyで使用した手法を利用する

triangle_elements = []

#
#   a   ->  A     
#  b c    
#
# 最小の三角形において頂点から下まで移動するときの数値の合計の最大値を求める
def getMaxOneTopNumber(top_number, b_left_num, b_right_num):
	return top_number + max(b_left_num, b_right_num)



# 要素を配列に格納
for line in open('triangle.txt', 'r'):
	triangle_elements.append(map(lambda x: int(x), line.replace('\r\n', '').split(' ')))


# トップダウンで求めるのではなく、ボトムアップで最大値を求めていく
# 最大値の計算回数がΣ(n-1)回で終わらせることができる
for x in xrange(len(triangle_elements) -2 , -1, -1):
	row_elements = triangle_elements[x]
	comp_elements = triangle_elements[x+1]

	# 要素を最大値で書き換える
	for y in xrange(len(row_elements)):
		triangle_elements[x][y] =  getMaxOneTopNumber(row_elements[y], comp_elements[y], comp_elements[y+1])

print triangle_elements[0][0]
