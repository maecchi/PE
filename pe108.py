#e!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe108.py - Project Euler
#
# 1/x + 1/y + 1/n を式変形すると
# (x-n)(y-n) = n^2
# このときn^2の約数の個数をNとすると
# xとyの組み合わせは(N+1)/2個存在する((x-n)=(y-n)=nの時以外入れ替え可能な点より)
# n^2の約数は素因数分解を用いて
# n = p1^e1*p2^e2*...*pn^enと表すことができるならば
# n^2 = p1^(2*e1)*p2^(2*e2)*...*pn^(2*en)なので
# 約数の個数は
# (2*e1+1)*....*(2*e2+1)と表すことができる
from itertools import *
from math import sqrt

LIMIT = 500
NUM_OF_SOL = 1000

def generatePrimeFactors():
	# 素因数pを使用した数と残りの値を返却する
	def divPow(n, p):
		e = 0
		while n % p == 0:
			e += 1
			n /= p
		return e, n

	start = 2
	while True:
		a = range(start, start+LIMIT)
		# 素因数分解リスト
		# b[k]に数字nにおける (p,m)のタプル配列が格納 p:素因数, m:pの出現回数
		b = [[] for k in xrange(start, start+LIMIT)]
		# takewhile(a,b): aが真である限りbから要素を返すイテレータを作成
		# 素数の2乗が上限を超えない
		for p in takewhile(lambda p : p * p < start+LIMIT, prime_list):
			if p >= start:
				begin = p * 2
			else:
				begin = (start + p - 1) / p * p
			for n in xrange(begin, start+LIMIT, p):
				k = n - start
				e, a[k] = divPow(a[k], p)
				b[k].append((p,e))

		# LIMIT分の数だけ探索範囲を追加する
		for k in xrange(LIMIT):
			n = start + k
			# 数字に対して未定義状態=>素数リストに追加
			if len(b[k]) == 0:
				b[k] = [(n,1)]
				prime_list.append(n)
			elif a[k] > 1: # 1でない場合は素数が残っているので素因数分解リストに格納
				b[k].append((a[k],1))

		for f in b:
			yield f

		start += LIMIT

# 解の総数を返却する
def getSolutions(f):
	def c(f, k):
		if k == len(f):
			return 1
		else:
			return (f[k][1] * 2 + 1) * c(f, k + 1)
	
	return (c(f,0) + 1) / 2

prime_list = []

# dropwhile(a,b): aが真である限りは要素を無視し、その後は全ての要素を返すイテレータを作成する
# izip(a*): 各aの要素をまとめるイテレータを作成する
# imap(a,b*):  b* の要素を引数としてfunction aを呼び出すイテレータを作成
print dropwhile(lambda x:x[1] <= NUM_OF_SOL, izip(count(2), imap(getSolutions, generatePrimeFactors()))).next()[0]
