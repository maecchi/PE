#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe004.py - Project Euler
#

max_palindrome = 0

for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		is_palindrome = True
		palindrome_factor = []
		product = i * j
		save_product = product

		# 既に回文数の方が値が大きい場合は調査の必要はなし
		if (product < max_palindrome):
			break

		# 回文数であるかを確認
		while product > 0:
			palindrome_factor.append(product%10)
			product = int(product / 10)
			
		factor_len = len(palindrome_factor)
		if factor_len > 1:
			for k in range(0, int(factor_len/2)):
				if (palindrome_factor[k] != palindrome_factor[factor_len - k - 1]):
					is_palindrome = False
					break
		# for文を通過したものが回文数
		if (is_palindrome and max_palindrome < save_product):
			max_palindrome = save_product
			break
print 'max:', max_palindrome
