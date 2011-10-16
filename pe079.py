#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe079.py - Project Euler
#
# トポロジカルソートを使用する

used_dic = {}
graph = [[False for i in xrange(10)] for x in xrange(10)]
visited = [False for n in xrange(10)]

for line in open('keylog.txt', 'r'):
	line = line.replace('\r\n', '')
	x, y, z = map(lambda x: int(x), list(line))
	used_dic[x] = used_dic[y] = used_dic[z] = True
	graph[x][y] = graph[y][z] = True


# トポロジカルソート
def visit(v):
	if visited[v] == True:
		return
	visited[v] = True
	
	for x in xrange(10):
		if not (x in used_dic) or graph[x][v] == False:
			continue
		visit(x)
	print v

for v in xrange(10):
	if v in used_dic:
		visit(v)
