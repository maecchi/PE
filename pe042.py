#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe042.py - Project Euler
#

words_list = []
triangle_number_set = set([1])
count = 0

def isTriangleNumber (num):
	global triangle_number_set

	if num in triangle_number_set:
		return True
	
	set_length = len(triangle_number_set)

	while max(triangle_number_set) < num:
		triangle_number = set_length * (set_length+1) / 2
		triangle_number_set.add(triangle_number)
		set_length += 1
		
	if num == max(triangle_number_set):
		return True
	else:
		return False

for line in open('words.txt', 'r'):
	words_list = words_list + line.split(',')

# アスキーコードの差分をアルファベットのスコアとする
for word in words_list:
	word_score = sum(map(lambda x: ord(x) - ord('A') + 1, list(word.replace('"', ''))))
	if isTriangleNumber(word_score):
		count += 1

print count

