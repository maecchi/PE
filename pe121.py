#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe121.py - Project Euler
#
# ゲームに勝利する確率について分子と分母を分けて考える
from itertools import *
from math import *

# ゲーム回数
N = 15
# 分子格納
numerators = []

# 分母を求める関数
def getDenominator(N):
	return reduce(lambda x, y: x*y, (range(2, N+1+1)))


# 分母を求める
# ゲーム回数N においてr回青を引いたとき、勝利する確率の分子は
# 1からNまでの要素集合においてN - floor((N/2) + 1)個分、数字を取得し、その取得した数字の乗算の総和に等しい
# ゲーム回数が４回のとき３回青を引いて勝つ確率の分子は 1 + 2 + 3 + 4 = 10
for blue in xrange(int(floor(float(N)/2)+1), N+1):
	r = N - blue 
	numerator = 1
	if r == 0:
		numerators.append(numerator)
		continue

	for comb in combinations(range(1, N+1), r):
		numerators.append(reduce(lambda x,y : x*y, comb))
		#print (reduce(lambda x,y : x*y, comb))
		
print int(floor(getDenominator(N) / sum(numerators)))
