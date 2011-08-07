#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe055.py - Project Euler
#

LIMIT = 10000

count = 0
# 数字が回文数であるかを判定する
def isPalindrome (number):
	digit_number = list(str(number))
	reverse_digit_number = digit_number[::-1]

	return digit_number == reverse_digit_number


def checkPalindrome(number):
	for x in xrange(1, 50):
		number += int(''.join(list(str(number))[::-1]))
		if isPalindrome(number):
			return True
	
	return False

		
for x in xrange(1, LIMIT):
	if not checkPalindrome(x):
		count += 1

print count
