#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe107.py - Project Euler
#
from math import sqrt
from itertools import *
network_list = []
unreach_cost = '-'
INF = 10**12 # ダミー数字

def strToIntOnlyNumber(a):
	if a == '-':
		return a
	
	return int(a)

def getTotalNetworkCost(n_list):
	cost = 0
	n_len = len(n_list)
	for x in xrange(n_len):
		for y in ifilter(lambda a: n_list[x][a] != '-', xrange(x+1, n_len)):
			cost += n_list[x][y]
			
	return cost

# Minimum Spanning Tree
# 引数距離行列の配列
def MST(n_list):
	t_cost = 0
	edges = []

	# 集合の初期化
	X = set([0])
	Y = set(range(len(n_list))[1:])

	# 要素iに対する各その他の要素に行くためのコストはn_list[i][j] (1 <= j <= 39)
	# 要素0は最初の位置として使っているため探索に使用しない
	while len(Y) != 0:
		cost = INF
		edge = None
		for x in X:
			for y in Y:
				if n_list[x][y] != unreach_cost and cost > n_list[x][y]:
					cost = n_list[x][y]	
					edge = [x,y]
	
		#print "[MST]: minimum path is", edge
		X.add(edge[1])
		Y.remove(edge[1])

		t_cost += cost
		edges.append(edge)

	return t_cost, edges

# テキスト読み込み
for line in open('network.txt', 'r'):
	network_list.append(map(strToIntOnlyNumber, line.replace('\r\n', '').split(',')))

# 最小コスト
mst_list = MST(network_list)

# 辺の重みの総和
total_cost = getTotalNetworkCost(network_list)

# 節約量
print total_cost - mst_list[0]
