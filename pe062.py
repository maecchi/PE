#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe062.py - Project Euler
#
answer = 0
sort_str_cube_list = {}
n = 1
while(1):
	cube = n ** 3
	sort_str_cube = "".join(sorted(list(str(cube))))

	# 数字列を昇順に並べた文字列をキーとして値に立方数を代入する
	if sort_str_cube in sort_str_cube_list:
		sort_str_cube_list[sort_str_cube].append(cube)
	else:
		sort_str_cube_list[sort_str_cube] = [cube]

	if len(sort_str_cube_list[sort_str_cube]) == 5:
		answer = sort_str_cube_list[sort_str_cube][0]
		break

	n += 1

print answer
