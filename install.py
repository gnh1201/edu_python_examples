#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  install.py
#  Install requirement packages
#  

def main():
	pip.main(['install', 'turtle'])

	print "Installation Completed."
	return 0

if __name__ == '__main__':
	import pip
	main()
