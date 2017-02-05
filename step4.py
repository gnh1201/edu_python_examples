#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  step4.py
#  Check status of some point in square shape
#  

def move_turtle_to(position):
	turtle.up()
	turtle.goto(position[0], position[1])
	turtle.down()

def draw(shape):
	a = shape[0]
	b = shape[1]

	move_turtle_to([-(a/2), (b/2)])

	turtle.forward(a)
	turtle.right(90)
	turtle.forward(b)
	turtle.right(90)
	turtle.forward(a)
	turtle.right(90)
	turtle.forward(b)
	turtle.right(90)

def main():
	shape = [100, 50]
	draw(shape)

	a = raw_input("Input dots location (x, y): ")
	b = a.split(",")

	c_x = int(b[0].strip())
	c_y = int(b[0].strip())

	print c_x

	move_turtle_to([c_x, c_y])
	turtle.dot(5)

	min_x = 0 - (shape[0] / 2)
	max_x = shape[0] + (shape[0] / 2)

	min_y = 0 - (shape[1] / 2)
	max_y = shape[1] - (shape[1] / 2)

	in_x = False
	in_y = False

	if c_x >= min_x and c_x <= max_x:
		in_x = True
	if c_y >= min_y and c_y <= max_y:
		in_y = True

	if in_x == True and in_y == True:
		print "Dot dose exists in square."
	else:
		print "Dot dose not exists in square."

	return 0

if __name__ == '__main__':
	import turtle
	main()

