#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe031.py - Project Euler
#

LIMIT = 200
coins = [200, 100, 50, 20, 10, 5, 2, 1]
# 支払い方法の数を格納する配列を作成
# way[i] に i ポンドに対する支払い方法の総数が入る
ways = [1] + [0] * LIMIT

# 支払い方法が限定される大きい通過から走査を行う
for coin in coins:
	for i in range(coin, LIMIT+1):
		ways[i] += ways[i-coin]

print ways[LIMIT]
