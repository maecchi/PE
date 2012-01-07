#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe092.py - Project Euler
#

LIMIT = 10000000
answer = 0
loopend_list = {}

# ループの最終到達数を返す
def checkLastNumber(num):
	global loopend_list
	base_num = num
	is_loopend = False
	check_list = [1,89]

	if not num in check_list:
		while(is_loopend == False):
			num = sum(map(lambda x:pow(int(x),2), list(str(num))))
			if num in loopend_list:
				num = loopend_list[num]
				is_loopend = True
			elif num in check_list:
				is_loopend = True
	
	loopend_list[base_num] = num
	
	return num


for x in xrange(1, LIMIT):
	if checkLastNumber(x) == 89:
		answer += 1

print answer
