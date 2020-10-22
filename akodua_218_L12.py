#Albert Kodua
#G01139458

class Pokemon:
	def __init__(self, name, species, combat_power, can_fly):
		self.name = name
		self.species = species
		self.combat_power = combat_power
		self.can_fly = can_fly
		
	def __str__(self):
		return "Pokemon('" + str(self.name) + "'), '"  + str(self.species) + "', " + str(self.combat_power) + ')'
	
	def __repr__(self):
		return "Pokemon('"  + str(self.name) + "'), '"  + str(self.species) + "', " + str(self.combat_power) + ')'
	
	def __eq__(self, other):
		if self.name == other.name and self.species  == other.species and self.combat_power == other.combat_power:
			return True
		else:
			return None
	
	def battle(self, other):
		if self.combat_power > other.combat_power:
			return True
		if self.combat_power == other.combat_power and ((self.species != "Flying") or (other.species != "Flying")): 
			return None
		elif (self.species == "Flying"):
			return self.species
		elif (other.species == "Flying"):
			return other.species
		else:
			return False

class Pokebox:
	
	def __init__(self, members=None):
		if(members = None):
			self.members = []
	
	def __str__(self):
		
		