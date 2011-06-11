#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe022.py - Project Euler
#

name_list = []
score_total = 0
for line in open('names.txt', 'r'):
	name_list = line.split(',')

sort_name_list = sorted(name_list)

rank = 1
# アスキーコードの差分をアルファベットのスコアとする
for x in range(len(sort_name_list)):
	score_total += (x+1) * sum(map(lambda x: ord(x) - ord('A') + 1, list(sort_name_list[x].replace('"', ''))))

print score_total
