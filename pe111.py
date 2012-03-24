#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe111.py - Project Euler
#
# 10桁の数字を生成(重複数字は9個から走査)
# 素数判定、素数だったら対象値を残す
# S(10,d)を算出する
# S(10,d)(0<=d<=9)の総和を求める

from random import seed, randrange
from itertools import *

# ミラーラビン法
def Miller_Rabin(n):
    if n % 2 == 0:
        return False
    
    def MR_core(d, a, s = 1):
        if s == 1:
            return MR_core(d >> 1, a, 2) == n
        elif s == 2:
            if d & 1:
                m = MR_core(d >> 1, a, 3)
                s = m * m % n * a % n
                return n if s == n - 1 or s == 1 else s
            else:
                m = MR_core(d >> 1, a, 2)
                if m == n:
                    return n
                else:
                    s = m * m % n
                    return n if s == n - 1 else s
        elif s == 3:
            if d == 0:
                return 1
            else:
                m = MR_core(d >> 1, a, 3)
                if d & 1:
                    return m * m % n * a % n
                else:
                    return m * m % n
    
    k = 3
    return all(MR_core(n - 1, randrange(2, n)) for i in range(k))

# 文字列リストを数字列にして返却する
def str2Num(str_list):
	return reduce(lambda x,y : 10 * x + y, str_list)


def S(d):
	
	# 重複する数字以外の箇所がm個ある数字列を生成する(重複数字が0のとき)
	def generateNumber0(m):
		for a in combinations(range(1, N), m - 1):
			yield (0,) + a
			

	# 重複する数字以外の箇所がm個ある数字列を生成する(m=0のとき以外)
	def generateNumber(m):
		if d == 0:
			g = generateNumber0(m)
		else:
			g = combinations(range(N), m)
		for a in g:
			# product(A, B) は ((x,y) for x in A for y in B) 
			# product(A, repeat) = product(a,b,...) for a in A for b in A ....)
			for b in product(range(d) + range(d+1, 10), repeat = len(a)):
				# 頭が0の数字は対象にならない
				if b[0] == 0 and a[0] == 0:
					continue;
				# 重複数字がN個あるリストを作成
				c = [d] * N
				# 要素をまとめてイテレータで返す
				for x,y in izip(a, b):
					# xには対象要素番号, yには置き換える数字が入る
					c[x] = y
				# 文字列を数字にして返す
				yield str2Num(c)

	# 重複する数字以外の箇所がm個のとき条件に当てはまる数字の総和をもとめる:w
	def partS(m):
		# 素数のみの総和を返却
		return sum(filter(Miller_Rabin, generateNumber(m)))
		
	# imap(func, iterable): iterablesの要素を引数としてfuncを呼び出す
	# a.next():コンテナ内の次の要素を返す
	return ifilter(lambda s: s > 0, imap(partS, count(1))).next()


N = 10
print sum(S(d) for d in range(10))
