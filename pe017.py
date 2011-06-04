#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe017.py - Project Euler
#
# 最初はダミー
from_1_to_19_strs = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# 最初と２番目の要素はダミー
from_20_to_90_strs = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# 数値の英単語を格納する配列
number_string_array = []

for x in xrange(1, 1000):
	number_str = ''

	# 百の位の英単語確認
	if (int(x / 100)) :
		hundred_digit = int(x / 100)
		number_str = from_1_to_19_strs[hundred_digit] + 'hundred'
		x = x % 100
		if x:
			number_str = number_str + 'and'

	# 一,十の位の英単語確認
	if x < 20:
		number_str = number_str + from_1_to_19_strs[x]
	else :
		ten_digit = int(x / 10)
		one_digit = x % 10
		number_str =  number_str + from_20_to_90_strs[ten_digit] + from_1_to_19_strs[one_digit]

	number_string_array.append(number_str)

# 1000の数字だけ別処理
number_string_array.append('onethousand')

# 文字列のリストを文字列長のリストに変換、その後文字列長の総和を求める
print sum(map((lambda x: len(x)), number_string_array))
