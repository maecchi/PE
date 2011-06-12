#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe025.py - Project Euler
#
fibonacci_elements = []
digit_length = 0
number = 0
max_digit_length = 1000

def fibonacci(n, fibonacci_elements):
	if n <= 2:
		return 1
	else:
		if len(fibonacci_elements) > n-1:
			return fibonacci_elements[n-2] + fibonacci_elements[n-3]
		else:
			return fibonacci(n-1, fibonacci_elements) + fibonacci(n-2, fibonacci_elements)

while digit_length < max_digit_length:
	number += 1
	fibonacci_number = fibonacci(number, fibonacci_elements)
	fibonacci_elements.append(fibonacci_number)

	digit_length = len(str(fibonacci_number))

	
print number
