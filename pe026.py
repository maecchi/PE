#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe026.py - Project Euler
#

digit_element = []
max_recurringcycle = 0
max_recurringchcle_number = 1
target_max_number = 1000

# 循環節の長さを返却する関数
# 循環節がないときは0を返す
def getRecurringCycle(number):
	# キー：商の余り, 値:小数桁数の配列を作成する
	digit_elements = [0] * number
	decimal_rank = 0
	divided_number = 1

	while divided_number > 0:
		decimal_rank += 1
		divided_number = divided_number * 10


		divided_number = divided_number % number
		if digit_elements[divided_number] != 0:
			break;

		digit_elements[divided_number] = decimal_rank

	return decimal_rank - digit_elements[divided_number]

for number in xrange(2, target_max_number + 1):
	recurringcycle = getRecurringCycle(number)
	if recurringcycle > max_recurringcycle:
		max_recurringcycle = recurringcycle
		max_recurringcycle_number = number

print max_recurringcycle_number, max_recurringcycle
