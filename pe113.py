#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe113.py - Project Euler
#
# 重複組み合わせで考える
# n種から重複を許してr個取る組み合わせ
# nHr = (n+r-1)Cr
# 
# 0を含めて増加数を考えると
# 0が0個 -> M桁の増加数
# 0が1個 -> M-1桁の増加数
# 0が2個 -> M-2桁の増加数
# ...
# 0がM個のときは正数ではないので省略する
# よって増加数は10種から重複を許してM個とる組み合わせ数になる
# (10)H(M) = (10+M-1)C(M) = (M+9)C(9)
# (nCr = nC(n-r)より)
# 0がM個のときは除くので(M+9)C(9) - 1
#
# 減少数は0を使う
# 増加数と同様に桁数を決定する番兵のようなものをイメージして11種類考えればよい
# よって減少数は11種類から重複を許してM個取る組み合わせ数
# (11)H(M) = (11+M-1)H(M) = (M+10)C(10)
# 番兵がM個のとき、番兵と0のみの組み合わせのときは省くから(M=3のときMMMは取らない:数にならないため)
# (M+10)C(10) - 1 - M

# 組み合わせ総数を求める(itertools.combinationsは組み合わせ総数を求めるには速度が遅い...)
def comb(n, r):
	if r == 0:
		return 1
	else:
		return comb(n,r-1) * (n-r+1)/r

# 増加数を求める
def getSumIncNum(M):
	return comb(M+9, 9) - 1 

# 減少数を求める
def getSumDecNum(M):
	return comb(M+10, 10) - 1 - M


# 増加数と減少数には333など数字が同一の値がともに出てくるので重複分を引く(9*M個分)
NUM = 100
print getSumIncNum(NUM) + getSumDecNum(NUM) - 9*NUM


