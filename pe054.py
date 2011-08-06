#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe054.py - Project Euler
#
### 役一覧
# 役なし
# One Pair
# Two Pair
# Three Card
# Straight
# Flush
# Full House
# Four Card
# Straight Flush
# Royal Straight Flush
p1_win =0
p2_win = 0
draw = 0

def highCard(num_list):
	return max(num_list)

def isOnePair(num_list):
	if len(set(num_list)) == 4:
		return True
	
	return False

def isThreeCard(num_list):
	if len(set(num_list)) == 3:
		# ソート後の配列の真ん中の要素がThreeCardの番号
		three_num = sorted(num_list)[2:-2][0]

		count = 0
		for x in num_list:
			if x == three_num:
				count += 1
		if count == 3:
			return True
	return False

def isTwoPair(num_list):
	if len(set(num_list)) == 3 and not isThreeCard(num_list):
		return True
	return False

def isStraight(num_list):
	if len(set(num_list)) == 5:
		# ソート後の文字列化した数字を結合した文字列が
		# 1から15の数字を結合した文字列の一部であればよい
		if ''.join(map(str, sorted(num_list))) in ''.join(map(str, xrange(1, 15))):
			return True
	return False

def isFlush(pt_list):
	if len(set(pt_list)) == 1:
		return True
	return False

def isFourCard(num_list):
	if len(set(num_list)) == 2:
		if len(set(sorted(num_list)[1:-1])) == 1:
			return True
	return False

def isFullHouse(num_list):
	if not isFourCard(num_list) and len(set(num_list)) == 2:
		return True
	return False

def isStraightFlush(num_list, pt_list):
	if isStraight(num_list) and isFlush(pt_list):
		return True
	return False

def isRoyalStraightFlush(num_list, pt_list):
	if isStraightFlush(num_list, pt_list) and 14 in num_list and 10 in num_list:
		return True
	return False

# アルファベットを数字に変換
def convertNumber(cards):
	num_list = []
	for x in cards:
		if x[0] == 'T':
			num_list.append(10)
		elif x[0] == 'J':
			num_list.append(11)
		elif x[0] == 'Q':
			num_list.append(12)
		elif x[0] == 'K':
			num_list.append(13)
		elif x[0] == 'A':
			num_list.append(14)
		else:
			num_list.append(int(x[0]))
	return num_list

def rmmax(num_list):
	max_num = max(num_list)
	num_list.remove(max_num)
	return max_num

def rnum(num, num_list):
	while num in num_list:
		num_list.remove(num)

# 手柄を確認する
# 手柄は数値化する
# 役に応じて15をx乗する
def checkHand(num_list, pt_list):
	if isRoyalStraightFlush(num_list, pt_list):
		return 15**9

	if isStraightFlush(num_list, pt_list):
		last_num = rmmax(num_list)
		return 15**8 + last_num

	if isFourCard(num_list):
		t_num = sorted(num_list)[2:-2][0]	
		rnum(t_num, num_list)
		r_num = rmmax(num_list)
		return (15**7)*t_num + r_num

	if isFullHouse(num_list):
		t_num = sorted(num_list)[2:-2][0]
		rnum(t_num, num_list)
		r_num = num_list[0]
		rnum(r_num, num_list)
		return 15**6*t_num + r_num
		
	if isFlush(pt_list):
		max_num = rmmax(num_list)
		return 15**5 + max_num

	if isStraight(num_list):
		last_num = rmmax(num_list)
		return 15**4 + last_num

	if isThreeCard(num_list):
		t_num = sorted(num_list)[2:-2][0]
		rnum(t_num, num_list)
		r_num = rmmax(num_list)
		return 15**3*t_num + r_num

	if isTwoPair(num_list):
		nums = list(set(num_list))
		cp_list = [x for x in num_list]
		for i in nums:
			cp_list.remove(i)
		rnum(cp_list[0], num_list)
		rnum(cp_list[1], num_list)
		r_num = rmmax(num_list)
		return 15**2*cp_list[0] + 15**2*cp_list[1] + r_num
	
	if isOnePair(num_list):
		nums = list(set(num_list))
		cp_list = [x for x in num_list]
		for i in nums:
			cp_list.remove(i)
		rnum(cp_list[0], num_list)
		r_num = rmmax(num_list)
		return 15**1*cp_list[0] + r_num
	return rmmax(num_list)
		

for line in open('poker.txt', 'r'):
	card_list = line.rstrip("\r\n").split(' ')

	p1_list = card_list[0:5]
	p1_num = convertNumber(p1_list)
	p1_pt = [x[1] for x in p1_list]

	p2_list = card_list[5:10]
	p2_num = convertNumber(p2_list)
	p2_pt = [x[1] for x in p1_list]

	p1_hand_score = checkHand(p1_num, p1_pt)
	p2_hand_score = checkHand(p2_num, p2_pt)

	if p1_hand_score > p2_hand_score:
		p1_win += 1
   	elif p1_hand_score == p2_hand_score:
		while len(p1_num) and len(p2_num):
			p = rmmax(p1_num)
			q = rmmax(p2_num)
			if p > q:
				cnt += 1
				break
	else:
		p2_win += 1
	if not len(p1_num) and not len(p2_num):
		draw += 1  


print p1_win, p2_win, draw

