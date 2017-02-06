#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  step3.py
#  Lottery with Two-length number
#

def generate_lottery_number():
	a = random.random()
	b = int(a * 100)

	return b

def number_format(number):
	a = locale.format(u'%d', number, True)

	return a

def main():
	prizes = [10000000, 3000000, 1000000, 0]
	str_nums = str(generate_lottery_number())
	lucky_num = raw_input("Input your lucky number: ")

	real_nums = list(str_nums)
	choiced_nums = list(lucky_num)
	
	# create code
	codes = []
	for i in range(len(real_nums)):
		for k in range(len(choiced_nums)):
			if real_nums[i] == choiced_nums[k]:
				codes.append(1)
			else:
				codes.append(0)
	code_sum = sum(codes)

	# verify matrix
	c_prize = 3
	if code_sum >= 2:
		if (codes[0] + codes[3]) == 2:
			c_prize = 0
		else:
			c_prize = 1
	elif code_sum < 2 and code_sum >= 1:
		c_prize = 2
	else:
		c_prize = 3

	# print
	result_prizes = number_format(prizes[c_prize])

	print "correct number is: " + str_nums;
	if c_prize == 0:
		print "completed matched: you got " + result_prizes + " won!"
	elif c_prize == 1:
		print "inordered matched: you got " + result_prizes + " won!"
	elif c_prize == 2:
		print "one number matched: you got " + result_prizes + " won!"
	else:
		print "you not matched."

	return 0

if __name__ == '__main__':
	import random
	import locale
	locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

	main()

