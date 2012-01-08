#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# name.py - Project Euler
#
import itertools as it

# 数字の組み合わせは10C4通り

LIMIT = 10
anspair = []
answer = 0

# 四則演算の結果を返す
# na: 数字nの分子
# nb: 数字nの分母
# ma: 数字mの分子
# mb: 数字mの分母
def evalOne((na,nb), symbol, (ma,mb)):
	if symbol == '+':
		return (na * mb + nb * ma, nb * mb)
	elif symbol == '-':
		return (na * mb - nb * ma, nb * mb)
	elif symbol == '*':
		return (na * ma, nb * mb)
	else:
		return (na * mb, nb * ma)
		
# 計算結果を返す関数
# eval_order: 計算の順番。右の要素番号のsignの位置から順に計算が行われる
def evalAll(order_list, signs, eval_order):
	if eval_order == (0,1,2):
		return evalOne( evalOne( evalOne( (order_list[0],1), signs[0], (order_list[1],1) ), signs[1], (order_list[2],1) ), signs[2], (order_list[3],1) )
	elif eval_order == (0,2,1) or eval_order == (1,2,0):
		return evalOne( evalOne( (order_list[0],1), signs[0], (order_list[1],1) ), signs[1], evalOne( (order_list[2],1), signs[2], (order_list[3],1) ) )
	elif eval_order == (1,0,2):
		return evalOne( evalOne( (order_list[0],1), signs[0], evalOne( (order_list[1],1), signs[1], (order_list[2],1) ) ), signs[2], (order_list[3],1) )
	elif eval_order == (2,0,1):
		return evalOne( (order_list[0],1), signs[0], evalOne( evalOne( (order_list[1],1), signs[1], (order_list[2],1) ), signs[2], (order_list[3],1) ) )
	elif eval_order == (2,1,0):
		return evalOne( (order_list[0],1), signs[0], evalOne( (order_list[1],1), signs[1], evalOne( (order_list[2],1), signs[2], (order_list[3],1) ) ) )
	return eval_order, "none"

def getNumbers():
	n = 1
	while (True):
		yield n
		n += 1


for num_list in it.combinations(xrange(LIMIT),4):
	# 数集合
	s = set()
	# ４つの数の順序順に走査
	for order_list in it.permutations(num_list, 4):
		# 四則演算子も順番に使用
		for signs in it.product("+-*/", "+-*/", "+-*/"):
			for eval_order in it.permutations(xrange(3)):
				# 分子と分母毎に算出
				(nume, deno) = evalAll(order_list, signs, eval_order)
				if (nume * deno > 0) and (deno != 0) and (nume % deno == 0):
					s.add(nume/deno)
	
	g = getNumbers()
	for n in g:
		# 連続した数の生成が途切れるとき
		if n not in s:
			# 連続した数は今までの最大連続数を超えているか
			if answer < n - 1:
				anspair = num_list
				answer = n - 1
			break

print anspair , answer
				
