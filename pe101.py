#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe101.py - Project Euler
#
# 
# 生成関数F(n)に対してnを大きくすることで要素nの数字列を作成
# 数字列nから生成される生成関数F'(n)におけるF'(n+1)の値を全部足していけば値は求まる
# 
# のだが、今回はNumpyを使用して考えてみる
from numpy import *
from numpy.linalg import inv

x = range(1,11)
y = [1- n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10 for n in x]
answer = 0

for i in range(1,11):
	answer += polyval(inv(vander(x[:i])) * mat(reshape(y[:i], (i,1))), i+1)[0]

print int(round(answer))
