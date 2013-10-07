"""
This segment of code completes some exercises from Chapter 4 of Think Python.

Author: Aliesha Garrett
"""

from swampy.TurtleWorld import *
import math

#draws a square
def square(bob):

	world=TurtleWorld()
	bob=Turtle()
	print bob

	for i in range(4):
		fd(bob,100)
		lt(bob)


#draws a square of given length sides
def lsquare(length):

	world=TurtleWorld()
	bob=Turtle()
	print bob

	for i in range(4):
		fd(bob,length)
		lt(bob)


#draws a polygon with n sides of given length
def polygon(n,length):

	world=TurtleWorld()
	bob=Turtle()
	print bob

	for i in range(n):
		fd(bob,length)
		lt(bob, 360/n)




#draws a circle with radius r
def circle(t,r):
	import math

	length= math.pi*r/180
	t.delay=.01

	for i in range(360):
		fd(t,length)
		rt(t, 1)




#draws an arc of a circle with radius r and angle a
def arc(t,r,a):

	world=TurtleWorld()
	t=Turtle()
	t.delay=.01
	print t

	length= math.pi*r/180
	

	for i in range(a):
		fd(t,length)
		lt(t, 1)


def star(t,length):
	for i in range(5):
		fd(t,length)
		lt(t,72)
		fd(t,length)
		rt(t,144)


def circle_star(t,length):
	t.delay=.01
	star(t,length)
	lt(t,72.4)
	a=length*math.sin(.314159265)
	circle(t,length+a)


world=TurtleWorld()
t=Turtle()
length=50

circle_star(t,length)

