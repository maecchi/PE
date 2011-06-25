#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe029.py - Project Euler
#
terms = set()
max = 100

for a in xrange(2, max+1):
	for b in xrange(2, max+1):
		term = pow(a,b)
		if not term in terms:
			terms.add(term)

print len(terms)
