
#-------------------------------------------------------------------------------

# TASK 0 (example)

# EXAMPLE: this function is implemented for you, to show 
# what a function definition looks like, and how the
# 'student' added four lines to complete the definition.

def is_even(n):
	# at the end, we'll return whatever current value
	# that's in ans as our return value. Somewhere in 
	# this function, you should re-assign it to be
	# either True or to False.
	ans = None
	
	# make decisions with if-else structures to determine
	# whether n is even (divisible by two) or not. Then,
	# set ans to equal True or equal False as your answer.
	
	# YOUR CODE GOES HERE. (Since it's an example, we've
	# already written "your code" - four lines).
	
	if n % 2 == 0 :
		ans = True
	else:
		ans = False
	
	# make this the last line of your function definition
	return ans

#-------------------------------------------------------------------------------

# TASK 1

# given a non-negative integer, this function returns a
# string (it does not print!) matching the letter grade
# for our class (check the syllabus).

def letter_grade(score):
	# starting value for variable ans. Change it before
	# the end of the function.
	
	if score >= 98 <= 100:
		ans = "A+"
	elif score >= 92 < 98:
	    ans = "A"
	elif score >= 90 < 92:
		ans = "A-"
	elif score >= 88 < 90:
		ans = "B+"
	elif score >= 82 < 88:
		ans = "B"
	elif score >= 80 < 82:
		ans = "B-"
	elif score >= 78 < 80:
		ans = "C+"
	elif score >= 72 < 78:
		ans = "C"
	elif score >= 70 < 72:
		ans = "C-"
	elif score >= 60 < 70:
		ans = "D"
	elif score >= 0 < 60:
		ans = "F"
	
	
	# YOUR CODE GOES HERE. Figure out what string you want
	# to assign to the ans variable, and assign it.
	
	
	# leave this as the last line of your function.
	return ans

#-------------------------------------------------------------------------------
# TASK 2

# without calling the max(), min(), or any sorting functionality,
# this function determines the two largest values of the three 
# and returns their sum. The integers might be negative. When
# there's a tie between two numbers, it doesn't actually matter
# which one you choose.

def sum2biggest(a, b, c):
	# starting value for variable ans. Replace it with the
	# actual answer integer before reaching the return stmt.
	
	
	ans = None
	largest_num = 0
	medium_num = 0
	
	if (a >= b) and (a >= c):
		largest_num = a
		
	elif (b >= a) and (b >= c):
		largest_num = b
		
	else:
		largest_num = c
	
	if(largest_num == a):
		if (b <= a) and (b >= c):
			medium_num = b
		else:
			medium_num = c

# if b is the largest number
	if(largest_num == b):
		if (a <= b) and (a >= c):
			medium_num = a
		else:
			medium_num = c		
	
	if(largest_num == c):
		if (a <= c) and (a >= b):
			medium_num = a
		else:
			medium_num = b	
	
	# find the sum of the two largest values. Re-assign the
	# answer to the ans variable.
	# YOUR CODE GOES HERE
	
	# leave this as the last line of your function.
	ans = largest_num + medium_num
	
	return ans

#-------------------------------------------------------------------------------


