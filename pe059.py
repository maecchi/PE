#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe059.py - Project Euler
#
#
# = 鍵となる文字を探す
#
part = [[] for i in xrange(3)]
secure_key = []
message = ''
answer = 0
# 数字の出現頻度を数え上げて、多い順に並べて返す。
def count(num_array):
	h = {}
	for n in num_array:
		if not h.has_key(n):
			h[n] = 1
		else:
			h[n] += 1

	return sorted(h.items(), key=lambda x:x[1], reverse=True)

for line in open('cipher1.txt', 'r'):
	cipher_arr = map(lambda x : int(x), line.split(","))

# text_arr を鍵の同じ文字に対応する 3 つの部分に分ける。
for x in xrange(len(cipher_arr)):
	part[x % 3].append(cipher_arr[x])
	
# 各パートで頻出する 5 文字を " " に見立てて鍵の文字を推測する。
for p in part:
	tmp =  map(lambda x: chr((x[0] ^ ord(' '))), count(p)[:5])
	secure_key.append(tmp[0])

# ASCII値を求める
for i in xrange(len(cipher_arr)):
	message += chr(ord(secure_key[i % 3]) ^ cipher_arr[i])
print message

for i in xrange(len(cipher_arr)):
	answer += (ord(secure_key[i % 3]) ^ cipher_arr[i])
print answer
