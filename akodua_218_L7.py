# Albert Kodua
# G01139458
# CS 112

def rank3(x,y,z, ascending = True):
    #A new list is created.
	new_list = [x,y,z]
	#The list is then sorted based on ascending
	#or descending order, if the optional parameter
	#was included
	new_list.sort(reverse = not ascending)
	#the list is then converted into a tuple
	#and returned
	return tuple(new_list)

def remove(val,xs,limit=None):
	#If there is no limit, remove all
	#occurences of the value.
	if (limit == None):
		num = len(xs)
	#If there is a limit, set num = 0
	#This should create the new version
	#of xs.
	elif (limit < 0) or (limit == 0):
		num = 0
	#Else, set num equal to limit of
	#removals
	else:
		num = limit
	index = 0
	#Removes the duplicate value
	while (val in xs) and (index < num):
		xs.remove(val)
		index += 1
def filter_chars(msg, keeps=''):
	#Sets the new string as an empty string
	string_new = ''
	#If keeps is an empty string by default,
	#a for loop goes through and searches for
	#letters, discarding any non-letters.
	if keeps == '':
		for index in msg:
			if index.isalpha():
				string_new += index
	#If there is a string in keeps, whether the letters are
	#uppercase or lowercase, add this to the new string. 
	#Discards the other letters.
	else:
		for index in msg:
			if (index.lower() in keeps) or (index.upper() in keeps):
				string_new += index
	#Returns the new string.
	return string_new


def relocate_evens(data,new_home=[]):
    #If new home is an empty list and the number in the data
	#list is even, that number is added to new home.
	if new_home==[]:
		even=[index for index in data if (index%2==0)]

		new_home=even
    #Else, if new home is not an empty list,
	#if the number in the index is even, remove it from data
	#and add it to new home
	else:
		for index in data:
			if index%2==0:
				data.remove(index)
				new_home.append(index)
	#set indx to 0
	indx = 0

	#While going through data, remove each even number.
	while indx in range(0,len(data)):
		if data[indx] in new_home:
			data.remove(data[indx])
			indx = indx - 1

		indx += 1

	return new_home