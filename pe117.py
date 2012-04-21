#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe117.py - Project Euler
#

# 定数
N = 50


# 組み合わせ総数のリストを求める
numbers = [1]
for n in range(1, N+1):
	numbers.append(sum(numbers[k] for k in xrange(max(0, n-4), n)))


print numbers[N]
