# car class object
class Car(object):

	def __init__(self, ctype, model, name):
		self.name = name
		self.ctype = ctype
		self.model = model



def find_details():

	honda = Car('Honda','HND-9009','Verrosa')

	if isinstance(honda, Car):
		return 'The object should be an instance of the `Car` class'

	if type(honda) is Car:
		return 'The object should be a type of `Car`'

print find_details()
