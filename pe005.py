#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe005e.py - Project Euler
#


# 対象の値を素因数で割っていき、値が1になるまで続ける
def getPrimeFactors(number):
	factor_elements = {}
	factor = 1
	while number > 1:
		factor += 1
		if not number % factor: # 対象の素因数で割り切れるときは商の値を使用する
			count, quotient = getMultiplier(number, factor)
			factor_elements[factor] = count
			number = quotient
	return factor_elements;

# 第１引数の値を第２引数の値で割った結果を返す
def getMultiplier(number, divisible):
	count = 0
	quotient = number
	while quotient / divisible > 0: # 素因数で割り切れなくなるまで続ける
		count += 1;
		quotient = quotient / divisible

	return count, quotient


# 各々の全ての数で割り切れる値=各々の数の最小公倍数
answer = 1
prime_factors = {}
for i in range(1, 20):
	factors = {}
	if len(prime_factors) == 0:
		prime_factors[i] = 1
	else:
		factors = getPrimeFactors(i)
		for key, value in factors.iteritems():
			if key in prime_factors:
				if value > prime_factors[key]:
					prime_factors[key] = value
			else:
				prime_factors[key] = value
	
# prime_factorsに含まれている連想配列をkey^valueの乗算が求める最小公倍数
print prime_factors
for key, value in prime_factors.iteritems():
	answer = answer *  pow(key,value)

print "answer: ", answer
