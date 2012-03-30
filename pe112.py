#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe112.py - Project Euler
#

# 数字(リスト)がはずみ数であるか確認
def isBouncy(nums):
	is_inc, is_dec = False, False
	for i in range(len(nums) - 1):
		if nums[i] < nums[i+1]: 
			is_inc = True
		elif nums[i] > nums[i+1]:
			is_dec = True

		# 増加した状態と減少した状態両方ある場合ははずみ数
		# 数字が同じ値が続いた場合は変数がどちらもFalseになるので条件を満たさない
		if is_inc and is_dec:
			return True
	return False

n = 21780
percent = 0.9
# 27180の値までのはずみ数の総数は求められる
count = n * percent

while (percent != 0.99):
	n += 1
	nums = map(lambda x :int(x), list(str(n)))
	if isBouncy(nums):
		count += 1
	percent = float(count)/n

		
print n
