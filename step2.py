#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  step2.py
#  Convert Kilogram to Pounds
#  

def convert_kilo_to_pound(kilograms):
	pounds = kilograms * 2.2
	
	return pounds

def main():
	a = raw_input("please input pound: ")
	b = convert_kilo_to_pound(float(a))
	
	print("result is: " + str(b) + " pounds")
	
	return 0

if __name__ == '__main__':
	main()

