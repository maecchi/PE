#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe082.py - Project Euler
#

rows= []

for line in open('matrix.txt', 'r'):
	rows.append(map(lambda x: int(x), line.replace('\r\n', '').split(',')))

rows_key_max = len(rows)


def gen_neighbor(pt0):
	global rows_key_max
	x, y = pt0
	if x < rows_key_max - 1:
		yield x + 1, y
	if y > 0:
		yield x, y - 1
	if y < rows_key_max - 1:
		yield x, y + 1

def gen_not_arrived_neighbor(pt0):
	for pt in filter(lambda pt: pt not in exist, gen_neighbor(pt0)):
		yield pt

def insert(queue, s):
	pt, n = s
	for k in xrange(len(queue) - 1, -1, -1):
		if n > queue[k][1]:
			queue.insert(k + 1, s)
			return
	queue.insert(0, s)

def gen_min_path(s):
	global rows
	pt0, sum_path = s
	for pt in gen_not_arrived_neighbor(pt0):
		s = sum_path + rows[pt[1]][pt[0]]
		insert(queue, (pt, s))
		exist.add(pt)
		yield pt, s

def solve():
	global rows_key_max
	while True:
		for pt, min_path in gen_min_path(queue.pop(0)):
			if pt[0] == rows_key_max - 1:
				return min_path

exist = set([ (0, y) for y in range(rows_key_max) ])
queue = [ ((0, y), rows[y][0]) for y in range(rows_key_max) ]
queue.sort(key = lambda t: t[1])
print solve()
