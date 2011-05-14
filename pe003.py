#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe003.py - Project Euler
#

number = 600851475143
factor = 1

# 対象の値を素因数で割っていき、値が1になるまで続ける
while number > 1:
	factor += 1
	if not number % factor: # 対象の素因数で割り切れるときは商の値を使用する
		number =  number / factor

print factor
