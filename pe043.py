#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe043.py - Project Euler
#
# Pandigital数による数列を作成してから走査する
pandigitals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
MIN = 1023456789
MAX = 9876543210
total = 0

def checkNumber(num_str):
	mod2_check_num = int(num_str[1] + num_str[2] + num_str[3])
	mod3_check_num = int(num_str[2] + num_str[3] + num_str[4])
	mod5_check_num = int(num_str[3] + num_str[4] + num_str[5])
	mod7_check_num = int(num_str[4] + num_str[5] + num_str[6])
	mod11_check_num = int(num_str[5] + num_str[6] + num_str[7])
	mod13_check_num = int(num_str[6] + num_str[7] + num_str[8])
	mod17_check_num = int(num_str[7] + num_str[8] + num_str[9])
	
	if (not mod2_check_num % 2) and (not mod3_check_num % 3) and (not mod5_check_num % 5) and (not mod7_check_num % 7) and (not mod11_check_num % 11) and (not mod13_check_num % 13) and (not mod17_check_num % 17):
		return True
	else:
		return False

# Pandigital数の数列を返却する
def permutations(L):
    if len(L) == 1:
        yield [L[0]]
    elif len(L) >= 2:
        (a, b) = (L[0:1], L[1:])
        for p in permutations(b):
            for i in range(len(p)+1):
                yield p[:i] + a + p[i:]

for n in permutations(pandigitals):
	if n[0] == 0:
		continue
		
	num_str = map(lambda y: str(y), n)
	
	if (checkNumber(num_str)):
		total += sum([n[9-y] * pow(10,y)  for y in xrange(0, len(n))])

print total
