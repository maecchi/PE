#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe097.py - Project Euler
#
# べき乗するたびに10^10で割って桁数を少なくさせる

LIMIT_POW = 7830457

n = 1

for p in xrange(LIMIT_POW):
	n = n * 2 % pow(10,10)

n = (28433 * n + 1) % pow(10, 10)

print n
