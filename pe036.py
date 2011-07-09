#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe036e.py - Project Euler
#

LIMIT = 1000000
total = 0

# 引数の値が回文数であるかを確認
def isPalindromic (number):
	number_strs = list(str(number))
	number_len = len(number_strs)

	if (number_len < 1):
		return True

	for k in xrange(0, int(number_len)):
		if (number_strs[k] != number_strs[number_len - k - 1]):
			return False

	return True


for i in xrange(1, LIMIT):
	if isPalindromic(i):
		if isPalindromic(format(i, 'b')):
			total += i

print total 
