#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe089.py - Project Euler
#
import re
# ローマ字辞書
roma_dic = {
	'CM': 900,
	'CD': 400,
	'M': 1000,
	'D': 500,
	'XC': 90,
	'XL': 40,
	'C': 100,
	'L': 50,
	'IX': 9,
	'IV': 4,
	'X': 10,
	'V': 5,
	'I': 1
}
priority_romans = ['CM', 'CD', 'M', 'D', 'XC', 'XL', 'C', 'L', 'IX', 'IV', 'X', 'V', 'I']
roman_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_char_lens = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
default_total_length = 0
min_total_length = 0

# 要素を配列に格納
for line in open('roman.txt', 'r'):
	target  =line.replace('\r\n', '')
	default_total_length += len(list(target))
	total = 0
	for ch in priority_romans:
		val = roma_dic[ch]
		target,count = re.subn(ch, '', target)
		total += count * val
	
	for i in xrange(0, len(roman_nums)):
		num = roman_nums[i]
		char_len = roman_char_lens[i]
		while total >= num:
			total -= num
			min_total_length += char_len

print default_total_length - min_total_length

