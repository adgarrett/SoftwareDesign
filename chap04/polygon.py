"""
This segment of code completes some exercises from Chapter 4 of Think Python.

Author: Aliesha Garrett
"""

#draws a square
def square(bob):
	from swampy.TurtleWorld import *

	world=TurtleWorld()
	bob=Turtle()
	print bob

	for i in range(4):
		fd(bob,100)
		lt(bob)


#draws a square of given length sides
def lsquare(length):
	from swampy.TurtleWorld import *

	world=TurtleWorld()
	bob=Turtle()
	print bob

	for i in range(4):
		fd(bob,length)
		lt(bob)


#draws a polygon with n sides of given length
def polygon(n,length):
	from swampy.TurtleWorld import *

	world=TurtleWorld()
	bob=Turtle()
	print bob

	for i in range(n):
		fd(bob,length)
		lt(bob, 360/n)




#draws a circle with radius r
def circle(t,r):
	from swampy.TurtleWorld import *
	import math

	world=TurtleWorld()
	t=Turtle()
	t.delay=.01
	print t

	length= math.pi*r/180
	

	for i in range(360):
		fd(t,length)
		lt(t, 1)




#draws an arc of a circle with radius r and angle a
def arc(t,r,a):
	from swampy.TurtleWorld import *
	import math

	world=TurtleWorld()
	t=Turtle()
	t.delay=.01
	print t

	length= math.pi*r/180
	

	for i in range(a):
		fd(t,length)
		lt(t, 1)

