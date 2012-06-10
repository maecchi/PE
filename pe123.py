#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe123.py - Project Euler
#
# pe120と同じ考え方で考える

# (p(n)-1)^n + (p(n)+1)^n ≡  r (mod p(n)^2)
#
# n が偶数のとき (p(n)-1)^n + (p(n)+1)^n をrで割った際の剰余は 2
# n が奇数のとき (p(n)-1)^n + (p(n)+1)^n をrで割った際の剰余は 2p(n)n
#
# よってnが奇数の時のみの剰余を考える
#
# 素数が小さいものから順に出す

from itertools import * 

# 素数列を生成する
def generatePrimes():
	a = [ True ] * L
	for p in (n for n in xrange(2, L) if a[n]):
		for k in xrange(p*2, L, p):
			a[k] = False # 素数じゃないならFalse
	primes = [ n for n in xrange(2, L) if a[n] ]
	for p in primes:
		yield p

	# 1(True)が入っている値に対して	
	for m in count(1):
		start = m * L
		end = start + L
		a = [True] * L

		# takewhile():テスト関数がTrueを返す限り入力イテレータから要素を返す
		for p in takewhile(lambda p : p * p < end, primes):
			k0 = (start + p - 1) / p * p - start
			for k in xrange(k0, L, p):
				a[k] = False

		for p in (start+k for k in xrange(L) if a[k]):
			primes.append(p)
			yield p


# 題意のmod計算結果を返す
def mod(n, p):
	# 奇数なら2p(n) 偶数なら 2
	return 2 if n % 2 == 0 else 2 * n * p %(p*p)

N = 10 ** 10
L = 10000

# izip():引数で受け取った複数のイテレータの要素をタプルに結合するイテレータを返す)
print next(n for n, p in izip(count(1), generatePrimes()) if mod(n,p) > N)
