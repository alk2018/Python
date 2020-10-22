#Albert Kodua
#G01139458

def recursive_len(xs):
	if not xs:
		return 0
	else:
		xs.remove(xs[0])
	return 1 + recursive_len(xs)
	
def lucas(n):

	if (n < 0):
		return None
	if (n == 0):
		return 2
	elif (n == 1):
		return 1
	else:
		return lucas(n - 1) + lucas(n - 2)
		

def remove_duplicates(msg):
	if (len(msg) < 2):
		return msg
	if msg[0]!=msg[1]:
		return msg[0] + remove_duplicates(msg[1:])
	else:
		return remove_duplicates(msg[1:])
		
def binary(n):

	if (n > 1):
		return binary(n//2) + str(n % 2);
	else:
		return str(n)