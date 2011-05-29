#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe015.py - Project Euler
#

# 掲題の問題は40本の道路の内20本を東に進む組み合わせを求める内容と等しい
x = 20
y = 20

def getCombination(n, x):
	return reduce(lambda x, y : x * y, range(1, n+1)) / (reduce(lambda x, y : x * y, range(1, x+1)) * reduce(lambda x, y : x * y, range(1, n-x+1)))


print getCombination(x+y, x)
