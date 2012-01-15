#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe096.py - Project Euler
#
from math import sqrt

COL = 9
ROW = 9
BROCK_S = int(sqrt(COL))

# 水平方向のマスの候補抽出
def getNeighborsHor(hor, n, grid):
	neighbors = []
	for y in xrange(ROW):
		neighbors.append(grid[hor][y])
	while n in neighbors: neighbors.remove(n)
	return neighbors

# 垂直方向のマスの候補抽出
def getNeighborsVer(ver, n, grid):
	neighbors = []
	for x in xrange(COL):
		neighbors.append(grid[x][ver])
	while n in neighbors: neighbors.remove(n)
	return neighbors
	
# 3x3ブロックのマスの候補抽出
def getNeighborsBrock(x, y, n, grid):
	neighbors = []
	s_x = int(x / BROCK_S) * BROCK_S
	s_y = int(y / BROCK_S) * BROCK_S

	for a in xrange(s_x, s_x+BROCK_S):
		for b in xrange(s_y, s_y+BROCK_S):
			neighbors.append(grid[a][b])
	
	while n in neighbors: neighbors.remove(n)
	return neighbors
	

# 使用済み数字リストを取得
def getNeighbors(x, y, n, grid):
	return list(set((getNeighborsHor(x, n, grid) +  getNeighborsVer(y, n, grid) + getNeighborsBrock(x, y, n, grid))))

# 可能性のある数字候補を算出する
def getPossibleNums(neighbors):
	possibles = set([x for x in xrange(1,10)])
	possibles = list(possibles - set(neighbors))
	return possibles

# 候補が候補リストに存在するか確認
def check(p, x, y):
	return p in getPossibleNums(getNeighbors(x,y,target_matrix[x][y], target_matrix))

# 探索関数
def search(x, y, possibles):
	if x >= COL or y >= ROW:
		return True

	if target_matrix[x][y] != 0:
		if y == 8:
			if check(target_matrix[x][y], x, y) and (search(x+1, 0, possibles)):
				return True
		else:
			if check(target_matrix[x][y], x, y) and (search(x, y+1, possibles)):
				return True
	else:
		for p in set(possibles[x][y]):
			if check(p, x, y):
				target_matrix[x][y] = p
				if y == 8:
					if not(search(x+1, 0, possibles)):
						target_matrix[x][y] = 0
					else:
						return True
				else:
					if not(search(x, y+1, possibles)):
						target_matrix[x][y] = 0
					else:
						return True
	return False
	

# 左上隅３桁の数を求める
def getUpperLeftNumbers(m):
	# 解を入れていく行列
	global target_matrix
	target_matrix = m
	# 候補リスト作成
	possibles = [[] for i in xrange(COL)]
	for x in xrange(0,9):
		for y in xrange(0,9):
			if m[x][y] == 0:
				possibles[x].append(getPossibleNums(getNeighbors(x, y, m[x][y], m)))
			else:
				possibles[x].append([])
		
	# 検索開始
	for x in xrange(0,9):
		for y in xrange(0,9):
			if target_matrix[x][y] == 0:
				search(x, y, possibles)
	
	# 題意の値を返す
	return int(str(target_matrix[0][0]) + str(target_matrix[0][1]) + str(target_matrix[0][2]))

	
answer = 0
i = 1

grid_list = []
sudoku_ele = []
grid_num = 0
target_matrix = [] 
for line in open('sudoku.txt', 'r'):
	if i % 10 == 1:
		sudoku_ele = []
	elif i % 10 == 9:
		sudoku_ele.append(map(lambda x: int(x), list(str(line.replace('\r\n', '')))))
		grid_list.append(sudoku_ele)
	else:
		sudoku_ele.append(map(lambda x: int(x), list(str(line.replace('\r\n', '')))))
	i += 1


for x in xrange(len(grid_list)):
	answer += getUpperLeftNumbers(grid_list[x])

print answer

