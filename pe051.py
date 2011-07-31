#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe051.py - Project Euler
#

# 対象数字に同一の数があった場合、素数走査する

LIMIT = 1000000
NUM_OF_PRIME = 8

# 探索リスト
proposition_list = [],
# 素数リスト
prime_list = []

def initPrimeList(number):
	global prime_list, proposition_list
	
	proposition_list = range(2, number)
	# 素数リスト
	prime_list.append(proposition_list.pop(0))
	
	# エラトステネスの篩を使用する
	while max(proposition_list) >= pow(prime_list[-1], 2) :
		proposition_list =  [i for i in proposition_list if i % prime_list[-1]]
		prime_list.append(proposition_list.pop(0))

	prime_list = prime_list + proposition_list

def getSameDigitNumber(num):
	use_hash = {
		0 : 0,
		1 : 0,
		2 : 0,
		3 : 0,
		4 : 0,
		5 : 0,
		6 : 0,
		7 : 0,
		8 : 0,
		9 : 0
	}
	num_str_list = list(str(num))
	
	for x in num_str_list:
		use_hash[int(x)] += 1

	# 重複する数字の数が最大になる数(3以上)を返す(同じ数がないときはFalseを返す)
	if max(use_hash.values()) < 3:
		return False
	return max(use_hash.iterkeys(), key=lambda k :use_hash[k])

# 題意を満たす素数のリストを返却する
def searchAnswer(num, same_num):
	global prime_list

	replace_prime_list = [num]

	
	replace_num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	replace_num_list.remove(str(same_num))

	for t_num in replace_num_list:
		r_num = int(str(num).replace(str(same_num), t_num))
		if r_num in prime_list and len(list(str(r_num))) == len(list(str(num))):
			replace_prime_list.append(r_num)

	return replace_prime_list


initPrimeList(LIMIT)

for num in xrange(1, LIMIT+1):
	same_num = getSameDigitNumber(num)
		
	if same_num != False and same_num in [0,1,2] and num in prime_list:
		replace_prime_list = searchAnswer(num, same_num)
		
		if len(replace_prime_list) == NUM_OF_PRIME:
			break;
		

print sorted(replace_prime_list)
