#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe014.py - Project Euler
#

# Collatzの条件式
def collatz(number):
	if number == 1:
		return number
	elif not number % 2 :
		number = number / 2
	else :
		number = 3 * number + 1

	return number

max_counter = 0
max_chain_number = 0
target_number = 1000000 
for number in range(1, target_number+1):
	divide_number = number
	counter = 0
	while divide_number > 1:
		counter += 1
		divide_number = collatz(divide_number)
	if max_counter < counter:
		max_counter = counter
		max_chain_number = number

print "Max Chain:" , max_counter
print "Max Chain Number:" , max_chain_number
