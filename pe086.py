#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe086.py - Project Euler
#
# 直方体の長さをx,y,z(x =< y =< z)としたとき最短距離は
# sqrt((x+y)^2+z^2)
#
# ピタゴラス数を使用する
# 3辺をa,b,cとするとき
# a = 2lmn, b = l(m^2 - n^2), c = l(m^2 + n^2)
# と表すことができる（m,nは整数 m > n, m+n は奇数, mとnは互いに素)

from itertools import imap, ifilter
from fractions import gcd
from math import sqrt

LIMIT = 10 ** 6

def getSum(M):
	def f(m):
		counter = 0
		for n in ifilter(lambda n : gcd(m,n) == 1, xrange(2 if m & 1 else 1, m ,2)):
			x = m * m - n * n
			y = 2 * m * n
			if x > y:
				x, y = y, x
			# ここまでで二つのピタゴラス数を定義(x < y)

			# 個数を求める
			for l in xrange(1, M/x + 1):
				z, w = x * l, y * l
				if w <= M:
					# 大きさをZが最大としたときの個数
					counter += z / 2
					if z * 2 > w:
						counter += z - (w - 1) / 2
				elif z <= M and w < z * 2:
					counter += (z * 2 - w + 2) / 2

		return counter

	# 大きさがMの場合の最大レンジで算出(分割した距離に重複がないようにする)
	return sum(imap(f, xrange(2, (M + 1)/2 + 1)))

# 二分探索
def binSearch(start, end):
	if end - start == 1:
		return start
	else:
		middle = (start + end - 1) /2
		n = getSum(middle)
		if n <= LIMIT:
			return binSearch(middle + 1, end)
		else:
			return binSearch(start, middle + 1)

num = 1
while True:
	c = getSum(num)
	if c > LIMIT:
		break
	num *= 2


print binSearch(num/2 + 1, num + 1)
