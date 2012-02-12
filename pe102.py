#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe102.py - Project Euler
#
# 三角形の各頂点をABCとしP(0,0)とすると
# 点Pが各辺AB,BC,CAに対して、同じ向きにあるならば
# 点Pは三角形ABCの内部にあるといえる

ele_list = []


def checkContains(elements):
	x1,y1,x2,y2,x3,y3 = elements

	ap = (-1*x1, -1*y1)
	ab = (x2-x1, y2-y1)
	
	bp = (-1*x2, -1*y2)
	bc = (x3-x2, y3-y2)

	cp = (-1*x3, -1*y3)
	ca = (x1-x3, y1-y3)

	# N1 = ap * ab
	n1 = ap[0] * ab[1] - ap[1] * ab[0]
	# N2 = bp * bc
	n2 = bp[0] * bc[1] - bp[1] * bc[0]
	# N3 = cp * ca
	n3 = cp[0] * ca[1] - cp[1] * ca[0]

	if (n1 < 0.0 and n2 < 0.0 and n3 < 0.0) or (n1 >= 0.0 and n2 >= 0.0 and n3 >= 0.0):
		return 1
	else:
		return 0
	


# テキスト読み込み
for line in open('102_triangles.txt', 'r'):
	ele_list.append( tuple(map(float, line.replace('\r\n', '').split(','))))

print sum(map(checkContains, ele_list))

