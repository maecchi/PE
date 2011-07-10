#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe040.py - Project Euler
#

MAX_DIGIT_OF_FRACTAL = 1000000

digit_of_fractal = 0
number = 1
fractal_digit_elements = [0]

while (digit_of_fractal < MAX_DIGIT_OF_FRACTAL):
	digit_of_fractal += len(str(number))
	str_number_list = list(str(number))
	fractal_digit_elements += map(lambda x: int(x), str_number_list)
	number += 1

print fractal_digit_elements[1] * fractal_digit_elements[10] * fractal_digit_elements[100] * fractal_digit_elements[1000] * fractal_digit_elements[10000] * fractal_digit_elements[100000] * fractal_digit_elements[1000000]

