#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe106.py - Project Euler
#
# 第一のルール(同一性)のテストが実施されない条件は
# 集合要素の各要素の大小関係が各要素において不変であること
# (集合A(a,b,c),集合B(d,e,f)において a>bなら c<d, e<fも成り立つこと)
from itertools import *

# 集合の大小関係テスト(すべての要素において 集合A < 集合B ならFalse)
def test1(A, B):
	for x,y in zip(A, B):
		if x > y:
			return True
	return False

# 集合の大小関係テスト(すべての要素において 集合A > 集合B ならFalse)
def test2(A, B):
	for x,y in zip(A, B):
		if x < y:
			return True
	return False

# 同一性のテストを行うか否か 
# 行う場合はTrue
def test(A, B):
	return test1(A, B) and test2(A, B)

# 同一性テストを行う数を返す
# n : 集合の要素数, 部分集合が持つ要素数
def getNumTest(n, m):
	counter = 0
	for A in combinations(range(n), m):
		# 使っていない要素リストを格納
		res = [0] * (n-m)
		k = 0
		l = 0
		for i in range(n):
			if k < m and A[k] == i:
				k += 1
			else:
				res[l] = i
				l += 1

		# 残りの要素を使ってm個の要素の部分集合を作成してテストをするか確認
		for B in combinations(res, m):
			if test(A, B):
				counter += 1
	# 集合A, 集合Bで使ったそれぞれの部分集合が逆転した組み合わせも含まれているため2で割る
	return counter / 2

def execNumberTest(n):
	# 2から(n/2+1)個の部分集合に対してgetNumTest()を使って同一性をテストする数をそれぞれ取得
	# その総和を返す
	return sum(map(lambda m : getNumTest(n,m) , range(2, n/2+1)))

N = 12
print execNumberTest(N)
