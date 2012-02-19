#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe104.py - Project Euler
#
# フィボナッチ数列問題

from itertools import *
from math import sqrt, log

# 数字の桁を配列に格納
def digits(n):
	def genDigits(n):
		while(n):
			n,r = divmod(n, 10)
			yield r
	return list(genDigits(n))

# フィボナッチ数列を生成
def genFib():
	a = 1
	b = 1
	while True:
		yield a
		a, b = b, a+b
	
# フィボナッチ数列剰余計算(引数：剰余数字)
def genFibMod(d):
	a = 1
	b = 1
	while True:
		yield a
		a, b = b, (a+b) % d

# パンデジタル数判定(1〜9までの数字を持つ)
# 各桁の数字を整数の各ビットに見立てて数字の和をとり1022になればよい
# num << x numの数字をx分だけ左にビットシフト
def isPandigital(ds):
	return sum (1 << d for d in ds) == 1022

# 下9桁の数がパンデジタル数であるか判定
def isLowerPandigital(n):
	return n % 9 == M and isPandigital(digits(n))

# 上9桁の数がパンデジタル数であるか判定
def isUpperPandigital(n, k):
	# フィボナッチ数列の一般項より桁数を算出
	e = int(( k * log((1 + sqrt(5)) / 2) - log(5) / 2) / log(10) - 0.4)
	m = n / 10 ** (e - N)
	while m >= D:
		m /= 10
	return isPandigital(digits(m))
	

# 題意を満たす数判定
def isValid(x):
	# f:フィボナッチ数列(F(n))の値 
	# f1: フィボナッチ数列(F(n))の下N桁の値
	f, f1 = x[1] 
	return isLowerPandigital(f1) and isUpperPandigital(f, x[0])


# izip(p, q) : イテレータを返す
# izip(p,q) = (p[0], q[0]), (p[1], q[1])...
# ifilter(predicate, iterable) : predicateがTrueになるiterableを返す
N = 9
M = N * (N+1) / 2 % 9
D = 10 ** N

# x[0] が求める要素番号
print (x[0] for x in ifilter(lambda x : isValid(x), izip(count(1), izip(genFib(), genFibMod(D))))).next()


