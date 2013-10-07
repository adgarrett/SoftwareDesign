"""This code creates a dragon curve.

Author: Aliesha Garrett

"""

import math
from swampy.TurtleWorld import *

def dragon(t, length, n):
	"""
	dragon draws a dragon curve.
	t: A turtle.
	length: Length of the steps- should be a positive 	integer.
	n: The number of recursions to go through. Should be 	a positive integer.
	"""
	fd(t,length)
	dragonx(t,length,n)

def dragonx(t,length,n):
	if n==0:
		return

	dragonx(t,length,n-1)
	rt(t)
	dragony(t,length,n-1)
	fd(t,length)


def dragony(t,length,n):
	if n==0:
		return
	fd(t,length)
	dragonx(t,length,n-1)
	lt(t)
	dragony(t,length,n-1)
	
	

def dragons(n):

	"""
	Builds a string with the steps process_string should 		take to draw a dragon curve.
	n: The number of recursions to go through. Should be 		a positive integer.
	"""
	if n == 0: return ""
	return "F"+dragonxs(n-1)

def dragonxs(n):
	if n==0:
		return ""

	
	return dragonxs(n-1)+"+"+dragonys(n-1)+"F"


def dragonys(n):
	if n==0:
		return ""
	return "F"+dragonxs(n-1)+"-"+dragonys(n-1)

def process_string(string,length,t):
	"""
	draws a dragon curve using the string built by 		dragons.
	t: A turtle.
	length: Length of the steps- should be a positive 	integer.
	string: the string returned by dragons.
	"""
	for char in string:
		if char == 'F':
			fd(t,length)
		elif char == '+':
			rt(t)
		elif char == '-':
			lt(t)






def hilbert(t, length, n):
	"""
	hilbert draws a hilbert curve.
	t: A turtle.
	length: Length of the steps- should be a positive 		integer.
	n: The number of recursions to go through. Should be 		a positive integer.
	"""
	fd(t,length)
	hilbertx(t,length,n)

def hilbertx(t,length,n):
	if n==0:
		return
	
	lt(t)
	hilberty(t,length,n-1)
	fd(t,length)
	rt(t)
	hilbertx(t,length,n-1)
	fd(t,length)
	hilbertx(t,length,n-1)
	rt(t)
	fd(t,length)
	hilberty(t,length,n-1)
	lt(t)


def hilberty(t,length,n):
	if n==0:
		return
	rt(t)
	hilbertx(t,length,n-1)
	fd(t,length)
	lt(t)
	hilberty(t,length,n-1)
	fd(t,length)
	hilberty(t,length,n-1)
	lt(t)
	fd(t,length)
	hilbertx(t,length,n-1)
	rt(t)








world=TurtleWorld()
t=Turtle()
length=5
t.delay=.01
n=100

gosper(t,length,n)

wait_for_user()
