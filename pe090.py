#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe090.py - Project Euler
#
import itertools

square_list = [[0,1], [0,4], [0,9], [1,6], [2,5], [3,6], [4,9], [6,4], [8,1]]

dices =  list(itertools.combinations(xrange(0,10),6))
paturn_num = len(dices)
answer = 0

# 6と9をダイスに追加する
def addReverse6or9(dice):
	dice = list(dice)
	if 6 in dice or 9 in dice:
		dice.append(6)
		dice.append(9)
	return list(set(dice))

# 総当たり方式
for i in xrange(0,paturn_num):
	dice1 = addReverse6or9(dices[i])
	for j in xrange(i, paturn_num):
		dice2 = addReverse6or9(dices[j])
		flag = True
		for k in xrange(0,9):
			if not (square_list[k][0] in dice1 and square_list[k][1] in dice2 or square_list[k][1] in dice1 and square_list[k][0] in dice2):
				flag = False
				break

		if (flag == True):
			answer += 1

print answer
