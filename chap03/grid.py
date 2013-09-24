"""Solution to an exercise in Think Python.

Author: Aliesha Garrett
"""

#Draws a grid with x by y squares where x and y are integers of 1 or greater

def draw(x,y):

	a='+ - - - -'*x
	b='|        '*x

	for i in range(y):	
	
		print a,'+'
		print b,'|'
		print b,'|'
		print b,'|'
		print b,'|'


	print a,'+'




#draws a 4X4 grid
def draw4():

	a='+ - - - -'*4
	b='|        '*4

	for i in range(4):	
	
		print a,'+'
		print b,'|'
		print b,'|'
		print b,'|'
		print b,'|'


	print a,'+'





#draws a 2x2 grid
def draw2():

	a='+ - - - -'*2
	b='|        '*2

	for i in range(2):	
	
		print a,'+'
		print b,'|'
		print b,'|'
		print b,'|'
		print b,'|'


	print a,'+'








