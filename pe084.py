#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe084.py - Project Euler
#
import random
LIMIT = 100000

# ボード配列
board = [
'GO', 'A1', 'CC', 'A2', 'T1', 'R', 'B1', 'CH', 'B2', 'B3',
'JAIL', 'C1', 'U', 'C2', 'C3', 'R', 'D1', 'CC', 'D2', 'D3',
'FP', 'E1', 'CH', 'E2', 'E3', 'R', 'F1', 'F2', 'U', 'F3',
'G2J', 'G1', 'G2', 'CC', 'G3', 'R', 'CH', 'H1', 'T2', 'H2'
]

record = {}
for m in xrange(len(board)):
	record[m] = 0

def dice(now):
	doubles = 0
	roll1 = random.randint(1,4)
	roll2 = random.randint(1,4)

	if (roll1 == roll2):
		doubles = 1

	now += roll1 + roll2
	if (now > 39):
		now = now - 39
	# JAIL行き
	if (now == 30):
		return (10, doubles)
	
	# CCのとき
	if board[now] == 'CC':
		com = random.randint(1,12)
		if com == 1:
			return (0, doubles)
		elif com == 2:
			return (10, doubles)

	# CHのとき
	if board[now] == 'CH':
		chance = random.randint(1,16)
		if chance == 1:
			return (0, doubles)
		elif chance == 2:
			return (10, doubles)
		elif chance == 3:
			return (11, doubles)
		elif chance == 4:
			return (24, doubles)
		elif chance == 5:
			return (39, doubles)
		elif chance == 6:
			return (5, doubles)
		elif chance == 7 or chance == 8:
			while board[now] != 'R':
				now = now + 1
				if now == 40:
					now = 0
			return (now, doubles)
		elif chance == 9:
			while board[now] != 'U':
				now = now + 1
				if now == 40:
					now = 0
			return (now, doubles)
		elif chance == 10:
			return (now-3, doubles)
		else:
			return (now, doubles)

	return (now, doubles)

now = 0
# ゾロ目
doubles = 0
# 試行開始
for i in xrange(LIMIT):
	temp = dice(now)
	
	# サイコロがゾロ目だった時
	if temp[1] == 1:
		doubles += 1
		# ゾロ目が3回目連続のとき
		if doubles == 3:
			now = 10
			record[now] += 1
			doubles = 0
			continue

	doubles = 0
	now = temp[0]
	record[now] += 1

sort_record = sorted(record.items(), key=lambda x:x[1], reverse = True)
answer_list = [str(key) for key,value in sort_record[:3]]
print ''.join(answer_list)
