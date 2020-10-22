# Albert Kodua
# G01139458
# I know this will be my lowest project grade, for sure.
def show(map):

	#List starts out as an empty list (map).
	list = []

	#Finds the number of rows and columns.
	xs = max([len(str(i2)) for i in map for i2 in i])

	#In a for loop, adds an extra space where needed in
	#the returned location.
	for i in map:

		space = [' '*(int(xs) - len(str(i2))) + str(i2) for i2 in i]

		list.append(" ".join(space))

	return ("\n".join(list) + "\n")
