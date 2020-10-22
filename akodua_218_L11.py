#Albert Kodua
#G01139458
#Token used

class Grade:
	def __init__(self, kind, name, percent):
		if (not kind in ["test", "lab", "project", "final"]):
			raise GradingError("no Grade kind '" + str(kind) + "'")
		self.kind = kind
		self.name = name
		self.percent = percent
	def __str__(self):
		return self.kind + ":" + self.name + "(" + str(self.percent) + "%)"
	def __repr__(self):
		return "Grade('" + self.kind + "', '" + self.name + "', " + str(self.percent) + ")" 
	def __eq__(self, other):
		return self.name == other.name and self.kind == other.kind and self.percent == other.percent

class GradingError(Exception):
	msg = ""
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return str(self.msg)
	def __repr__(self):
		return("GradingError(''"+repr(self.msg)+"'')")

class GradeBook:
	def __init__(self):
		self.grades = []
		
	def __str__(self):
		stri = 'GradeBook:\n'
		for grade in self.grades:
			stri += "\t" + str(grade) + '\n'
		return stri

	def __repr__(self):
		return str(self)

	def add_grade(self, grade):
		self.grades.append(grade)

	def average_by_kind(self, kind):
		count = 0
		total = 0.0
		for grade in self.grades:
			if grade.kind == kind:
				count += 1
				total += grade.percent
		if count == 0:
			return None
		else:
			return total / count

	def get_all_of(self, kind):
		same_kind_list = []
		for grade in self.grades:
			if grade.kind == kind:
				same_kind_list.append(grade)
		return same_kind_list

	def get_by_name(self, name):
		for grade in self.grades:
			if grade.name == name:
				return grade
		raise GradingError('no Grade found named ' + "'" + name + "'")
