#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe010.py - Project Euler
#
# 探索リスト
proposition_list = range(2, 2000000)
# 素数リスト
prime_list = []
prime_list.append(proposition_list.pop(0))

# エラトステネスの篩を使用する
while max(proposition_list) > pow(prime_list[-1], 2) :
	proposition_list =  [i for i in proposition_list if i % prime_list[-1]]
	prime_list.append(proposition_list.pop(0))

print sum(prime_list + proposition_list)
