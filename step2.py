#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  step2.py
#  Convert pounds to kilograms
#  

def convert_pound_to_kilo(pounds):
	kilograms = pounds * 0.454
	
	return kilograms

def main():
	a = raw_input("please input pounds: ")
	b = convert_pound_to_kilo(float(a))
	
	print("result is: " + str(b) + " kilograms")
	
	return 0

if __name__ == '__main__':
	main()

