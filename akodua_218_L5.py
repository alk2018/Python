#Albert Kodua
#G01139458
#Lab 5 - CS 112 (I request a token for this lab.)

def location(xs,key):
 #Takes each each element of the list and passes it through
 #the for loop. If key is found, the location of key is
 #returned.
 for increment in range(len(xs)):
		if (xs[increment] == key):
			value = increment
			return value
		else:	
			return None
	
def	fibonacci(n):
 #If n is 0 or 1, return 1 
	if (n == 0) or (n == 1):
		return 1
 #If n > 1, while the increment is less than n,
 # find the current, next, and new terms.
	else:
		increment = 2 
		current_term = 1
		next_term = 1
    
		while (increment <= n):
			new_term = current_term + next_term
			current_term = next_term
			next_term = new_term
			increment += 1
  
		return new_term

def int_sqrt(n):
    #Assign n(number) to num.
	num1 = n
	#Equations and loops used to derive num1.
    num2 = int((num1 + 1) / 2)
    while num2 < num1:
        num1 = int(num2)
        num2 = int((num1 + n / num1) / 2)
    return num1

def sum_evens_2d(xss):
    #Creates even_sume
	even_sum = 0
	#Go through the 2D lost and checks for eveness
	for value in xss:
		if isinstance(value, int) and (value%2 == 0):
			even_sum += value
		elif isinstance(value, list):
			even_sum += sum_evens_2d(value)
	return even_sum



