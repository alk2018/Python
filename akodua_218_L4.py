# Lab 4

def middle (a, b, c):

	ans = 0

	# if a is the middle number
	if (a <= b) and (a >= c):
		ans = a
	elif(a <= c) and (a >= b):
		ans = a
	#if b is the middle number
	elif (b <= c) and (b >= a):
		ans = b
	elif(b <= a) and (b >= c):
		ans = b
	#if c is the middle number
	elif (c <= a) and (c >= b):
		ans = c
	elif(c <= b) and (c >= a):
		ans = c
		
	return ans
#print(middle(-3, -1, -2))