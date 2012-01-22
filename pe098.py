#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe098.py - Project Euler
#
from math import sqrt,ceil,floor

answer = 0
word_list = None

# w1とw2がアナグラムであるかを判定
def isAnagram(w1, w2):
	return sorted(list(w1)) == sorted(list(w2))

# wordが数字に置き換えることができるか
# 長さが同じこと前提
def isCorrectReplace(word, number):
	w_l = list(word)
	n_l = map(lambda x: int(x), list(str(number)))
	
	# 各チェックリスト
	w_c_l = {}
	n_c_l = {}
	flag = True

	# dict作成
	for w in w_l:
		w_c_l[w] = ''
	for n in n_l:
		n_c_l[n] = ''

	for i in xrange(len(w_l)):
		# w_c_l確認
		if w_c_l[w_l[i]] == '':
			w_c_l[w_l[i]] = n_l[i]
		elif w_c_l[w_l[i]] != n_l[i]: # 対応する数字が複数できてしまった場合
			flag = False
			break
		
		# n_c_l確認
		if n_c_l[n_l[i]] == '':
			n_c_l[n_l[i]] = w_l[i]
		elif n_c_l[n_l[i]] != w_l[i]: # 対応する文字が複数できてしまった場合
			flag = False
			break

	return flag

# n桁の平方数を全て返す
def getDigitSqrt(n):
	if sqrt(n) % 1 != 0:
		return map(lambda x: x**2,  [x for x in xrange(int(ceil(sqrt(pow(10, n-1)))), int(floor(sqrt(pow(10,n) - 1)))+1)])
	else:
		return map(lambda x: x**2, [x for x in xrange(int(ceil(sqrt(pow(10, n-1)))), int(sqrt(pow(10,n))))])
		
# 平方数判定
def isSqrtNumber(n):
	if n == False:
		return False
	return sqrt(n) % 1 == 0

# word2とアナグラムになっているword1に対して対応した並び替え数字を返す
def getReplaceNumber(n, w1, w2):
	# w1は判定をしていない
	#if isCorrectReplace(w1, n) == False:
	#	return False
	w1_list = list(w1)
	w2_list = list(w2)
	n_list = list(str(n))
	
	assign_list = {}
	for i in xrange(len(w2_list)):
		assign_list[w2_list[i]] = n_list[i]
	
	ans = []
	for j in xrange(len(w1_list)):
		ans.append(assign_list[w1_list[j]])
	
	# 頭が0の場合はFalse
	if ans[0] == '0':
		return False
	else:
		return int(''.join(ans))
	

# 本文ここから
# リスト作成
for line in open('98_words.txt', 'r'):
	word_list =  map(lambda x : x.replace('"', ''), line.split(','))
	# 長さ順
	word_list.sort(key=(lambda x: len(x)))

max_str_length =  len(word_list[-1])
for l in xrange(2, max_str_length+1):
	# 長さxの要素リストを作成しアナグラム確認
	c_list = [x for x in word_list if len(x) == l]
	len_c_list = len(c_list)
	square_list = getDigitSqrt(l)
	for i in xrange(0, len_c_list-1):
		for j in xrange(i+1, len_c_list):
			if isAnagram(c_list[i], c_list[j]):
				# 平方数リストチェック
				for n in square_list:
					# c_list[j]は数字に置き換え可能?
					if isCorrectReplace(c_list[j], n) == False:
						continue

					# 置き換え数字 c_list[i], c_list[j]で平方数確認
					# c_list[i]に対する置き換え数字列を作成
					m = getReplaceNumber(n, c_list[i], c_list[j])
					if isSqrtNumber(m) == True:
						# 平方数だったら、最大の平方数を代入する
						answer = max(answer, n, m)

print answer
