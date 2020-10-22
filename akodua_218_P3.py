#Albert Kodua
#G01139458
#Token Used

def sum_divisors(n) :
    # Final result of summation of divisors 
    number = 0
    
    # find all divisors which divides 'num' 
    for i in range(2, n):
        if (n % i) == 0:
            number = number + i

    #if the number is 1 return 1.
    if(n == 1):
        return n

    # Add 1 and the number to the result as 1 is also a divisor 
    return ((number + 1) + n)

def pi(precision):
    #sets increment and pi_total as variables
	increment = 0 
	pi_total = 0 
	#infite loop 
	while True:
		#Lebinz Formula
		next_term = (4 * (-1) ** increment) / ((2 * increment) + 1) 
        #Adds the terms
		pi_total += next_term
        #Used to stop the next term from being lower than the precision
		if abs(next_term) <= precision:  
			break 
		increment += 1
	return pi_total 

def span(nums):
    #returns 0 as this would be an empty list
	if(len(nums) == 0):
		return 0
	else:
        #goes through each index of the list
		#to find the smallest and largest number
		min = nums[0]
		max = nums[0]
		#finds the largest and smallest numbers
		for val in nums:
            
			if(min > val):
				min = val
            
			if(max < val):
				max = val
        
		return (max - min)

def single_steps(nums):
	#sets result as starting value
	result = 0
	
	#loops to find differences and sums of 1 in the
	#indices
	for val in range(len(nums)-1):
	
	#adds and subtracts each neighboring index
		if (nums[val + 1] - nums[val] == 1):
			result = result + 1
		if (nums[val + 1] - nums[val] == -1):
			result = result + 1
	
	return result

def even_product_2d(grid):
	
	#If empty list or no even numbers are found
	#return one
	if(grid == [[]]):
		return 1
	
	#sets even_num to an empty list
	even_num = []
	
	#loops through indices to find even numbers
	for val in grid:
		for val2 in val:
			if((val2 % 2) == 0):
				even_num.append(val2)
	#sets final result equal to ine
	result = 1
	
	#gets the products of the even number
	for val in even_num:
		result *= val
	
	return result
	
def remove_echo(xs):
    #returns an empty list because the list 
	#is actually empty
	if (len(xs) == 0):
		return []
    #finds and removes duplicate characters
	else:
		index = [xs[0]]
		for val in range(len(xs)):
			if xs[val] != index[-1]:
				index.append(xs[val])
		return index