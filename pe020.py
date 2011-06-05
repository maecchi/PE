#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe020.py - Project Euler
#
# 題意の値
number_list = range(1,101)

product_number_list = reduce(lambda x,y: x * y, number_list)

# 文字列化してリスト分割
str_list = list(str(product_number_list))

# 文字列の要素を数値型に再変換し総和を求める
print sum(map((lambda x: int(x)), str_list))
