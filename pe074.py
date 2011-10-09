#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe074.py - Project Euler
#
LIMIT = 1000000
answer = 0
def getDigitPower(num):
	ans = 0
	digit_chars = map(lambda x: int(x), list(str(num)))
	for n in digit_chars:
		power = 1
		for i in xrange(1, n+1):
			power = i * power
		ans += power

	return ans


for n in xrange(1, LIMIT):
	count = 0
	power_dic = {}
	power_dic[n] = count
	circle_num = n
	while 1:
		count += 1
		circle_num = getDigitPower(circle_num)
		if circle_num in power_dic.keys():
			if count == 60:
				answer += 1
			break
		else:
			power_dic[circle_num] = count
		
print answer
