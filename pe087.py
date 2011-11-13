#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe087.py - Project Euler
#
from itertools import imap, ifilter
from math import sqrt
from random import seed, randrange

LIMIT = 50000000
PRIME_LIMIT = int(sqrt(LIMIT))
prime_list = [2]
pow_three_list = []
pow_four_list = []
count = 0
display_numbers = set()

def Miller_Rabin(n):
    if n % 2 == 0:
        return False
    
    def MR_core(d, a, s = 1):
        if s == 1:
            return MR_core(d >> 1, a, 2) == n
        elif s == 2:
            if d & 1:
                m = MR_core(d >> 1, a, 3)
                s = m * m % n * a % n
                return n if s == n - 1 or s == 1 else s
            else:
                m = MR_core(d >> 1, a, 2)
                if m == n:
                    return n
                else:
                    s = m * m % n
                    return n if s == n - 1 else s
        elif s == 3:
            if d == 0:
                return 1
            else:
                m = MR_core(d >> 1, a, 3)
                if d & 1:
                    return m * m % n * a % n
                else:
                    return m * m % n
    
    k = 3
    return all(MR_core(n - 1, randrange(2, n)) for i in range(k))

for n in xrange(2, PRIME_LIMIT):
	if Miller_Rabin(n):
		prime_list.append(n)


pow_three_list = [pow(n,3) for n in prime_list if pow(n,3) < LIMIT]
pow_four_list = [pow(n,4) for n in prime_list if pow(n,4) < LIMIT]


for tw in prime_list:
	pow_tw = tw * tw
	for th in pow_three_list:
		if pow_tw + th >= LIMIT:
			break
		for fo in pow_four_list:
			total = pow_tw + th + fo
			if total >= LIMIT:
				break
			elif total in display_numbers:
				# 既にカウントされた数はカウントしない
				continue
			else:
				display_numbers.add(total)
				count += 1

print count
