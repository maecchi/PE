#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# pe019.py - Project Euler
#
year_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_year = 1900
end_year = 2000 
counter = 0

# 曜日数の7の余剰数を求めることで題意の計算を行う
# 7の余剰が
# 0 : 日曜日
# 1 : 月曜日
# 2 : 火曜日
# 3 : 水曜日
# 4 : 木曜日
# 5 : 金曜日
# 6 : 土曜日
week_number = 1 # 週の番号

# 各月における先月との曜日のずれを計算
day_shift_year_days = map((lambda x: x % 7), year_days)
day_shift_leap_year_days = map((lambda x: x % 7), leap_year_days)


# ここから題意の計算
for x in xrange(start_year, end_year+1):
	use_year_days = day_shift_year_days

	if not x % 4:
		if x % 100 or not x % 400:
			use_year_days = day_shift_leap_year_days
	
	if x == 1900:
		# 来年の月初めの週の番号を計算
		week_number = (week_number + sum(use_year_days)) % 7
	else:
		for day_shift in use_year_days:
			if not week_number % 7:
				counter += 1

			# 来月の週の番号を計算
			week_number = (week_number + day_shift) % 7

print counter
