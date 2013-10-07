"""Solution for exercise 7.5 from Think Python.

Author: Aliesha Garrett
"""
import math

def estimate_pi():
		
	total=0
	count=0
	factor=((2*math.sqrt(2))/9801)
	term=1

	while term>10**-15:
		num=math.factorial(4*count)*(1103+26390*count)
		denom=math.factorial(count)**4*396**(4*count)
		term=factor*num/denom
		total= total+term
		count=count+1

	return 1/total

print estimate_pi()
