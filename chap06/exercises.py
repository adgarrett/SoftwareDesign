""" Solutions to exercises 7 and 8 of chapter 6 in Think Python

Author: Aliesha Garrett"""

def is_power(a,b):
	""" Determines if a is a power of b.
	
	a: number
	b: number
	"""
	if a%b!=0:
		return False
	elif a==b:
		return True
	else:
		return is_power(a/b,b)

def gcd(a,b):
	""" Returns the greatest common demoninator (gcd) of two 	numbers.

	a:number
	b:number
	"""
	r=a%b
	if r==0:
		return b
	else:
		return gcd(b,r)


