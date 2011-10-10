#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe077.py - Project Euler
#
from random import seed, randrange
# PE031と同様の考え方を行ってみる
LIMIT = 100
method = 5000
nums = [x for x in xrange(LIMIT, 0, -1)]
count = 2

# 数の表し方の方法の数を格納する配列を作成
# way[i] に 数iに対する支払い方法の総数が入る(1つの正整数で表す手法もカウントされている)
ways = [1] + [0] * LIMIT

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

# 方法が限定される大きい数から走査を行う
while ways[count] < method:
	if Miller_Rabin(count) or count == 2:
		for i in xrange(count, LIMIT+1):
			ways[i] += ways[i-count]

	count += 1

print count
