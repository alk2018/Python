#-------------------------------------------------------------------------------
# Name: Albert Kodua
# Project 2
# Due Date: 09/23/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, projects are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or 
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------

# this time, the template does not have as much guidance - please
# look at at the actual project specification for the rules and
# meanings of each function. You can modify any part of the template
# code to get the job done (abiding by the project's rules). For
# instance, you might want a different start value, or to use multiple
# return statements. This template is only offered in order to help
# you get started, it is not truly required in any sense for the 
# project. The function and parameter names must remain the same (e.g.,
# discount and age/major/is_in_military/gpa), but you can use any names you want
# inside of the functions (indented).


def discount(age, major, is_in_military, gpa):
	ans = False
	
	# If they are older than 65, they get a 20% discount.
	if (age >= 65):
		ans = True
	# If they are in the military, they get a 20% discount. 	
	elif (is_in_military == True):
		ans = True
	# If they are a Computer Science major AND have a 3.5+ GPA, 
	# they get a 20% discount.
	elif (major == "Computer Science") and (gpa >= 3.5):
		ans = True
	
	
	return ans

def calculate_cost(plan, num_minutes, num_text):
	
	#set the cost
	cost = 0
	add_cost1 = 0
	add_cost2 = 0
	
	#Basic Plan
	if (plan == "basic"):
		#Adds cost if there are additional minutes used
		if (num_minutes > 100) and (num_minutes%100 != 0):
			add_cost1 = (num_minutes%100) * 1.50
		elif (num_minutes%100 == 0):
			add_cost1 = (num_minutes - 100)* 1.50
		else:
			add_cost1 = 0
		
		#Adds cost if there are additional texts sent
		if (num_text > 1000) and (num_text%1000 != 0):
			add_cost2 = (num_text%1000) * 0.75
		elif (num_text%1000 == 0):
			add_cost2 = (num_text - 1000) * 0.75
		else:
			add_cost2 = 0
	
	#Standard Plan
	if (plan == "standard"):
		#Adds cost if there additional minutes used
		if (num_minutes > 175) and (num_minutes%175 != 0):
			add_cost1 = (num_minutes%175) * 1.25
		elif (num_minutes%175 == 0):
			add_cost1 = (num_minutes - 175)* 1.25
		else:
			add_cost1 = 0	
		
		#Adds cost if there are additional texts sent
		if (num_text > 1500) and (num_text%1500 != 0):
			add_cost2 = (num_text%1500) * 0.5
		elif (num_text%1500 == 0):
			add_cost2 = (num_text - 1500) * 0.5
		else:
			add_cost2 = 0
	
	#Premium Plan
	if (plan == "premium"):
		#Adds cost if there additional minutes used
		if (num_minutes > 250) and (num_minutes%250 != 0):
			add_cost1 = (num_minutes%250)
		elif (num_minutes%250 == 0):
			add_cost1 = (num_minutes - 250)
		else:
			add_cost1 = 0	
		
		#Adds cost if there are additional texts sent
		if (num_text > 2000) and (num_text%1000 != 0):
			add_cost2 = (num_text%2000) * 0.25
		elif (num_text%2000 == 0):
			add_cost2 = (num_text - 2000) * 0.25
		else:
			add_cost2 = 0	
		
	if (plan == "basic"):
		cost = 15 + add_cost1 + add_cost2
	if (plan == "standard"):
		cost = 20 + add_cost1 + add_cost2
	if (plan == 'premium'):
		cost = 25 + add_cost1 + add_cost2
	
	
	return cost
	
def cost_efficient_plan(age, major, is_in_military, gpa, num_minutes, num_text):
	
	ans1 = False
	ans2 = ""
	
	#sets the cost and additional cost

	cost1 = 0
	cost2 = 0
	cost3 = 0
	add_cost1 = 0
	add_cost2 = 0
	add_cost3 = 0
	add_cost4 = 0
	add_cost5 = 0
	add_cost6 = 0
	
	#Basic Plan Calculations
	# If they are older than 65, they get a 20% discount.
	if (age >= 65):
		ans1 = True
	# If they are in the military, they get a 20% discount. 	
	elif (is_in_military == True):
		ans1 = True
	# If they are a Computer Science major AND have a 3.5+ GPA, 
	# they get a 20% discount.
	elif (major == "Computer Science") and (gpa >= 3.5):
		ans1 = True
	else:
		ans1 = False
	
	#Basic Plan
	#Adds cost if there are additional minutes used
	if (num_minutes > 100) and (num_minutes%100 != 0):
		add_cost1 = (num_minutes%100) * 1.50
	elif (num_minutes%100 == 0):
		add_cost1 = (num_minutes - 100)* 1.50
	else:
		add_cost1 = 0
		
	#Adds cost if there are additional texts sent
	if (num_text > 1000) and (num_text%1000 != 0):
		add_cost2 = (num_text%1000) * 0.75
	elif (num_text%1000 == 0):
		add_cost2 = (num_text - 1000) * 0.75
	else:
		add_cost2 = 0
	
	#Standard Plan
	#Adds cost if there additional minutes used
	if (num_minutes > 175) and (num_minutes%175 != 0):
		add_cost3 = (num_minutes%175) * 1.25
	elif (num_minutes%175 == 0):
		add_cost3 = (num_minutes - 175)* 1.25
	else:
		add_cost3 = 0	
		
	#Adds cost if there are additional texts sent
	if (num_text > 1500) and (num_text%1500 != 0):
		add_cost4 = (num_text%1500) * 0.5
	elif (num_text%1500 == 0):
		add_cost4 = (num_text - 1500) * 0.5
	else:
		add_cost4 = 0
	
	#Premium Plan
	#Adds cost if there additional minutes used
	if (num_minutes > 250) and (num_minutes%250 != 0):
		add_cost5 = (num_minutes%250)
	elif (num_minutes%250 == 0):
		add_cost5 = (num_minutes - 250)
	else:
		add_cost5 = 0	
		
	#Adds cost if there are additional texts sent
	if (num_text > 2000) and (num_text%100 != 0):
		add_cost6 = (num_text%2000) * 0.25
	elif (num_text%2000 == 0):
		add_cost6 = (num_text - 2000) * 0.25
	else:
		add_cost6 = 0	
			
		#Basic Plan
		cost1 = 15 + add_cost1 + add_cost2
		#Standard Plan
		cost2 = 20 + add_cost3 + add_cost4
		#Premium
		cost3 = 25 + add_cost5 + add_cost6
		
	#20% Discount
	if(ans1 == True):
		cost1 = cost1 * 0.8

	#Finds the best plan for the user		
	if(cost1 < cost2 < cost3) or (cost1 < cost3 < cost2):	
		ans2 = "basic"	
	elif(cost2 < cost3 < cost1) or (cost2 < cost1 < cost3):
		ans2 = "standard"
	elif(cost3 < cost2 < cost1) or (cost3 < cost1 < cost2):
		ans2 = "premium"	
	elif(cost1 == cost2):
		ans2 = "basic"	
	elif(cost2 == cost3):
		ans2 = "standard"			
	else:
		ans2 = "premium"
	
	return ans2	