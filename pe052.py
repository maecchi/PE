#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe052.py - Project Euler
#

is_get_answer = False
num = 1
answer = 0

def isSameNumber(num):
	str_num = sorted(list(str(num)))
	str_two_times_num = sorted(list(str(2 * num)))
	str_three_times_num = sorted(list(str(3 * num)))
	str_four_times_num = sorted(list(str(4 * num)))
	str_five_times_num = sorted(list(str(5 * num)))
	str_six_times_num = sorted(list(str(6 * num)))

	if str_two_times_num == str_num and str_three_times_num == str_num and str_four_times_num == str_num and str_five_times_num == str_num and str_six_times_num == str_num:
		return True
	else : 
		return False

while (is_get_answer == False):
	if isSameNumber(num):
		is_get_answer = True
		answer = num
	num += 1

print answer
