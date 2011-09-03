#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe061.py - Project Euler
#
octagonal_list = []
polygonal_list = []

def triangle(n):
	return (n * (n+1)) / 2

def square(n):
	return n * n

def pentagonal(n):
	return (n * (3*n-1)) / 2

def hexagonal(n):
	return n * (2 * n - 1)

def heptagonal(n):
	return (n * (5 * n - 3))/2

def octagonal(n):
	return n * (3 * n - 2)

def searchAnswer(c_list):
	for check_ele in c_list:
		flags = check_ele[0]
		old_array = check_ele[1]
		if len(old_array) == 7: # 解の候補が見つかった
			if old_array[-1] == old_array[0]: # 最後まで巡回的か確認
				answer = 0
				for n in xrange(6):
					answer += old_array[n] * 100 + old_array[n+1]
				print answer
			return True
		else:
			if len(old_array) == 0:
				return False
			new_list = makeNewList(flags, old_array)
			searchAnswer(new_list)

def makeNewList(flags, array):
	global polygonal_list
	answer = []
	for x in xrange(len(flags)):
		if flags[x]:
			continue
		
		if not array[-1] in polygonal_list[x]:
			continue

		values = polygonal_list[x][array[-1]]

		for val in values:
			if (val / 10) == 0:
				continue
			new_flags = [i for i in flags]
			new_flags[x] = True
			answer.append([new_flags, array + [val]])

	
	return answer

# 角数のリストを作成
funcs = [
lambda x: octagonal(x),
lambda x: heptagonal(x), 
lambda x: hexagonal(x), 
lambda x: pentagonal(x), 
lambda x: square(x),
lambda x: triangle(x)
]

for func in funcs:
	n = 1
	tmp_list = {}
	while(1):
		poly = func(n)
		n += 1

		if poly < 1000:
			continue
		elif poly > 9999:
			break
	
		key, val = divmod(poly, 100)
		if key in tmp_list:
			tmp_list[key].append(val)
		else:
			tmp_list[key] = [val]

	polygonal_list.append(tmp_list)

# 解を見つける
octagonal_list = polygonal_list[0]
for key, values in octagonal_list.iteritems():
	flag = [True, False, False, False, False, False]
	check_list = []
	for val in values:
		tmp = [flag, [key, val]]
		check_list.append(tmp)
		searchAnswer(check_list)

