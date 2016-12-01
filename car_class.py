''' 
	Car class
	with un implemented methods
'''

class Car(object):

	def __init__(self, color, engine_type, number_doors, transimission):
		self.color = color
		self.engine_type = engine_type
		self.number_doors = number_doors;
		self.transimission = transimission

	def set_color(self, color):
		self.color = color

	def get_color(self):
		return self.color

	def set_engine(self, engine_type):
		self.engine_type = engine_type

	def get_engine_type(self):
		return self.engine_type
