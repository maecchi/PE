#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe048.py - Project Euler
#
LIMIT = 1000

series = [pow(x,x) for x in xrange(1, LIMIT+1)]
total = sum(series)
total_str = str(total)
ten_digit_str = total_str[-10:]

print ten_digit_str
