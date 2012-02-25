#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe105.py - Project Euler
#
# pe103を参考にする
from itertools import *

sets_list = []

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

# 題意を満たす場合、配列の総和を返す
def getSumForIsValid(a):
	if isValid(a):
		return sum(a)
	else:
		return 0

# テキスト読み込み
for line in open('sets.txt', 'r'):
	sets_list.append(sorted(map(int, line.replace('\r\n', '').split(','))))

# 最適特殊和集合である集合の総和を求める
print sum(map(getSumForIsValid , sets_list))
