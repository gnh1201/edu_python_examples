#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  step1.py
#  Printtable Square Table
#

def main():
	a = []
	
	for row in range(0, 5):
		if row == 0:
			b = ["a", "a^2", "a^3"]
		else:
			b = []
			for col in range(1, 4):
				b.append(pow(row, col))
		a.append(b)
		
	# print
	for i in range(len(a)):
		line = ""
		for k in range(len(a[i])):
			line += str(a[i][k]) + "\t"
		print line

	return 0

if __name__ == '__main__':
	main()
