"""This code completes exercise 5.6.1 and 5.6.2 from Think Python.

Author: Aliesha Garrett

koch draws a Koch curve.
t: A turtle.
length: length of the Koch curve- should be a positive integer.

snowflake draws a snowflake using 3 koch curves.
t: A turtle.
length: length of one koch curve. should be a positive integer.
"""

import math
from swampy.TurtleWorld import *

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


def koch(t,length):
	t.delay=.01
	if length<3:
		fd(t, n)
		return
	koch(t,length/3)
	lt(t,60)
	koch(t,length/3)
	rt(t,120)
	koch(t,length/3)
	lt(t,60)
	koch(t,length/3)


def snowflake(t, length):
	t.delay=.01
	for i in range(3):
		koch(t,length)
		rt(t,120)





world=TurtleWorld()
t=Turtle()
length=20
n=5

draw(t, length, n)

wait_for_user()
