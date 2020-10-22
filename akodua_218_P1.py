# Name: Albett Kodua
# G#: G01139458
# Project 1
# Due Date: 09/09/2018
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

# assumes the following prices: 
#   one Headless Hat: two galleons
#   one Boxing Telescope: 12 sickles and 26 knuts
#   one Canary Cream: seven sickles
# 
# Conversion rates:
#   1 galleon == 17 sickles
#   1 sickle  == 29 knuts
#
# assume all three parameters (num_hats, num_tels, num_creams) are
# non-negative integers.

# calculate how many knuts to pay given the order, and return that amount.
	# if you did store your answer in ans, then this works:

def checkout(num_hats, num_tels, num_creams):
	# create more variables as needed
   
	# Headless Hats
	# Purchasing Headless Hats (galleons to sickles to knuts)
   hats_amount = (num_hats) * 34 * 29 
    
	#Boxing Telescopes

	# Purchasing Boxing Telescopes (sickles to knuts)
   tels_amount = (num_tels) * ((12 * 29) + 26)
	
	# Purchasing Canary Creams (sickles to knuts)
   creams_amount = (num_creams * 7 * 29)
   
   total = hats_amount + tels_amount + creams_amount
   
   return total
   
#print(str(checkout(3, 4, 5)) + " knuts")

# ------------------------------------------------------------------------------

# assume the minutes parameter is an non-negative integer.
# how many fortnights, days, hours, and minutes are included in that period?

def timing(minutes):

	# probably you should change these before returning, right?...
	
	# minutes to hours
	num_hours = (minutes//60)
	
	#hours to days
	num_days = minutes//(60*24)
	
	#days to fortnights
	num_forts = minutes//(60*24*14)
	
	#minutes remainder
	num_mins = (minutes%60)
	
	# as always you can name your variables what you want, but
	# if you use these names, this return statement is what we need.

		
	return (num_forts, num_days, num_hours, num_mins)
	
	
#print(timing(42000))