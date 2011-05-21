#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe007.py - Project Euler
#
prime_array = []
sum_of_array = len(prime_array)
number = 1

while (len(prime_array) < 10001) :
	is_prime = True
	number += 1

	if sum_of_array == 0:
		if number != 1:
			prime_array.append(number)
	else:
		for i in prime_array :
			if not number % i:
				is_prime = False
				break
		if is_prime:
			prime_array.append(number)
	sum_of_array = len(prime_array)
print prime_array[len(prime_array)-1]
