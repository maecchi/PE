#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe006.py - Project Euler
#

range_field = range(1, 101)
# 二乗数の和
sum_of_square = reduce(lambda x, y : x + pow(y, 2), range_field)
# 和の二乗
square_of_sum = pow(reduce(lambda x, y : x + y, range_field), 2)

print square_of_sum - sum_of_square

