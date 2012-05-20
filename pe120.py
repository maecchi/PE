#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe120.py - Project Euler
#
# (a-1)^n + (a+1)^n ≡  r (mod a^2)
#
# n が偶数のとき (a-1)^n + (a+1)^n をrで割った際の剰余は 2
# n が奇数のとき (a-1)^n + (a+1)^n をrで割った際の剰余は 2an
#
# よってnが奇数の時のみの剰余を考える
#
# a が奇数のとき 剰余の最大は a(a-1) (nの値に関係なく偶数になるため)
# a が偶数のとき 剰余の最大は a(a-2) (nの値に関係なく偶数になるため)

START = 3
LAST = 1000

def getRMax(a):
	return a*(a-2) if a % 2 == 0 else a*(a-1)

print sum(getRMax(a) for a in xrange(START, LAST+1))
