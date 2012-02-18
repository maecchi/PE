#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe103.py - Project Euler
#
# 題意の規則に乗っ取って条件を作成する

from itertools import *


N = 7

# 
def findsSum(a, n):
	if n == 0:
		return True
	elif len(a) == 0:
		return False
	elif n < 0:
		return False
	else:
		a2 = a[1:]
		return any((findsSum(a2, n - a[0]), findsSum(a2, n)))

# 部分集合の和が等しくてはならない
def condition1(a):
	def c2_core(b):
		s = sum(b)
		if s % 2 == 1:
			return True
		half = s / 2
		back = b[-1]
		n = half - back
		return not findsSum(b[:-1], n)
	
	n = len(a)
	return all(c2_core(b) for m in range(3, n+1) for b in combinations(a, m))
	

# 部分集合は多くの要素を含んでいた方が値が大きい
def condition2(a):
	n = len(a)
	return sum(a[:(n+1)/2]) > sum(a[n/2+1:])

# 条件を両方とも満たすか確認
def isValid(a):
	return condition2(a) and condition1(a)

# 集合を作成する
# a: 集合要素
# prev: 前の要素
# k: 対象要素番号
def genSets(a, prev = 0 , k = 0):
	if k == len(a):
		yield []
	else:
		begin = max(a[k] - 2, prev + 1) # -2から+1の範囲で次の値を考える
		if k == len(a) - 1:
			end = a[k] + 1
		else :
			end = min(a[k] + 1, a[k+1] - 1)

		for p in range(begin, end+1):
			for b in genSets(a, p, k+1):
				yield [p] + b

# 最小値を求める
def minimize(a):
	solutions = [b for b in genSets(a) if isValid(b)]
	return min(solutions, key = lambda a: sum(a))

# 次の最適集合を求める
def nextSet(a):
	n = len(a)
	b = a[n/2]
	return minimize([b] + [e + b for e in a])


a = reduce(lambda x, y : nextSet(x), range(2, N+1), [1])
print "".join(map(str, a))
