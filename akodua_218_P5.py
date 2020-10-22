#Albert Kodua
#G01139458

#Writes and opens the file and
#divides the fields by spaces and
#commas. Return false if an error is found.

def write_votes(db, filename):
	try:
		votes = open(filename, "w")
		votes.write("fifty_s, name, party, p_votes, e_votes\n")
	
		for fifty_s in db:
			for runner in db[fifty_s]:
				votes.write(st + "," + name(runner) + "," + pty(runner) +
					"," + str(p_votes(runner)) + "," + str(e_votes(runner)) + "\n")
		votes.close()
		return True
	except:
		return False

#Starts with an empty dictionary,
#taking and stripping out any extra
#spaces all while reading said abbreviations
#and adding to the dictionary.

def read_abbreviations(filename):
	votes_db = {}
	votes = open(filename)
	read = votes.readlines()[1:]
	votes.close
	for str in read:
		if str not in votes_db:
			lt = str.split(",")
			num = lt[1].strip()
			votes_db[lt[0]] = num
	return votes_db
