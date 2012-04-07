#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe114.py - Project Euler
#
# 一番左にあるタイルの位置(左端, 右端)で場合分けする。
# 長さNでの場合の数をf(N)とすると、
# f(N) = Σ _{0 <= i < j= 50} f(50-j-1)
# これを修正する
# タイルの長さは最低3ユニットなのでjの範囲は i+3 <= j <= 50
# j = 49,50 の時はf(0), f(-1)が発生する
# f(-1): タイルが右端から一つずれている(49)
# f(0) : 右端にぴったり重なっている
# これらも１通りで考えるのでf(-1) = f(0) = 1
# タイルが一つ以上敷かれていることを前提に考えているので、
# タイルを一枚も敷き詰めていない場合も含めると式は
# f(50) = Σ _{(i,j) 0 <= i <= 50, i+3 <= j <= 50} f(50-j-1) + 1


N = 50
# 途中で使用するf(N)を格納
numbers = [-1] * (N+1)


def getAnswer(n):
	if numbers[n] > 0:
		return numbers[n]
	if n <= 0:
		return 1
	
	numbers[n] =  sum([getAnswer(n-j-1) for i in xrange(0, n) for j in xrange(i+3, n+1)]) + 1
	
	return numbers[n] 


print getAnswer(N)
