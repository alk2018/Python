#Albert Kodua
#G01139458
#Token Used

class Line:
	#Set the initial def with four parameters not including self
	# and sets the instance variables
	def __init__(self, name, area_code, number, is_active = True):
		self.name = name
		self.area_code = area_code
		self.number = number
		self.is_active = is_active
	#Sets and returns the string of the area code, the number, and the name of the person
	#calling.
	def __str__(self):
		return str(self.area_code) + "-" + str(self.number) + "(" + str(self.name) + ")"
	#Sets and takes the string of Line class and uses the area code, the number, and the name of the person
	#calling.
	def __repr__(self):
		return "Line ('" + str(self.name) + "', " + str(self.area_code) + ", " + str(self.number) + ")"
	#Returns true or false if the number and area are the same
	def __eq__(self, other):
		if self.area_code == other.area_code and self.number == other.number:
			return True
		else:
			return False
	#Functions made to activate or deactivate a line.
	def activate(self):
		is_active = True
		
	def deactivate(self):
		is_active = False
		
class CallError(Exception):
	#Creates an error message whenever a Call error is raised
	msg = ""
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return str(self.msg)
	def __repr__(self):
		return("CallError('"+repr(self.msg)+"'')")
		
class Call():
	def __init__(self, caller, callee, length):
		#Raises Call Error if either object is false or both are equal
		#to one another.
		if self.caller.is_active==False:
			raise CallError(self.caller.__repr__())
		if self.callee.is_active==False:
			raise CallError(self.callee.__repr__())
		if self.caller==self.callee:
			raise CallError(self.caller.__repr__()+ " cannot call itself")
		if length < 0:
			raise CallError('negative call length:'+str(length))
		#Creates instance variables 
		self.caller = caller
		
		self.length = length
		self.callee = callee
		
		#Takes and returns string of the Call with the number calling and the number being called.
	def __str__(self):
		return "Call" + self.caller__repr__() + " "+self.callee.__repr__()
	def __repr__(self):
		return "Call" + self.caller__repr__() + " " + self.callee.__repr__()
		#Checks area code for locality
	def is_local(self):
		if self.callee.area_code==self.caller.area_code:
			return True
		else:
			return False
