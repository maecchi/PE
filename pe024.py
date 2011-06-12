#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe024.py - Project Euler
#
dic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1000000 - 1
digits_array = [0] * len(dic)
rest_order = target
answer = 0

def permutation(n):
	if n == 0:
		return 1
	else :
		return reduce((lambda x,y: x * y), xrange(1,n+1))

# n桁の順列総数はn!
# n桁において第1項目が0である数の総数は(n-1)!
# 題意の値を(n-1)!で割った際の商が既に辞書順において走査済のn桁目の個数
length = len(dic)
while length > 0:
	divide = int(target / permutation(length-1))
	rest =  target % permutation(length-1)
	rest_order = rest
	
	digits_array[length-1] = dic[divide]
	del dic[divide]
	length -= 1
	target = rest


ten_pow = 0
for number in digits_array:
	value = number * pow(10, ten_pow)
	answer += value
	ten_pow += 1

print answer
