#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe083.py - Project Euler
#

from Queue import PriorityQueue

matrix= []

for line in open('matrix.txt', 'r'):
	matrix.append(map(lambda x: int(x), line.replace('\r\n', '').split(',')))

row_len = len(matrix)
col_len = len(matrix[0])

# 隣接する座標を返却する
def getNeighbor(x,y):
	if x > 0:
		yield x-1, y
	if x < row_len -1:
		yield x+1, y
	if y > 0:
		yield x, y-1
	if y < col_len -1:
		yield x, y+1


dists = [ [10**9] * col_len for n in range(row_len)]
q = PriorityQueue()
q.put((matrix[0][0], (0,0)))

while True:
	s, (x,y) = q.get()
	# 終了条件
	if (x,y) == (row_len - 1, col_len -1):
		break
	# 最小値ではなかったとき(既知のルートの値の方が小さい)
	if dists[x][y] <= s:
		continue

	dists[x][y] = s
	# x,yの隣接を取得
	for x1, y1 in getNeighbor(x,y):
		s1 = s + matrix[x1][y1]
		# 最小値ではなかったとき(既知のルートの値の方が小さい)
		if dists[x1][y1] < s1:
			continue
		q.put((s1, (x1, y1)))

print s
