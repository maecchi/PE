#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe058.py - Project Euler
#
# 題意を満たす条件において
# 辺の長さがn(nは奇数)のとき、各対角線頂点の値は
# n^2, n^2-(n-1), n^2-2(n-1), n^2-3(n-1)
from random import seed, randrange
SIDE_LIMIT = 30000
length = 3
diagonal_list = [[1]]
diagonal_prime_list = [0]
answer = 'MISSING'
sum_diagonal = 1
sum_diagonal_prime = 0

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


while (length < SIDE_LIMIT):
	prime_count = 0
	top_diagonals = [length**2, length**2-(length-1), length**2-2*(length-1), length**2-3*(length-1)]
	diagonal_list.append(top_diagonals)
	sum_diagonal += len(top_diagonals)

	for x in top_diagonals:
		if Miller_Rabin(x):
			prime_count += 1
	
	diagonal_prime_list.append(prime_count)
	sum_diagonal_prime += prime_count

	if (float(sum_diagonal_prime)) / float(sum_diagonal) * 100 < 10:
		answer = length
		break
	length += 2

print answer
