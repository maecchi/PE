#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe016.py - Project euler
#

base_number = pow(2, 1000)

# 文字列化してリスト分割
str_list =list(str(base_number))

# 文字列の要素を数値型に再変換し総和を求める
print sum(map((lambda x: int(x)), str_list))

