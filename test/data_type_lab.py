# function to check various input's data types
def data_type(d_type):
	# check if the supplied value is equal to none
	if d_type is None:
		return 'no value' 

	# test type if is a list and countthe number of element in it
	elif type(d_type) == list:
		size_list = len(d_type)
		if size_list >= 3:
			return d_type[2]
		else:
			return None

	# if the type is bool return True/False
	elif type(d_type) == bool:
		if d_type:
			return True
		else:
			return False

	# if the input is an integer determine either > or < 100

	elif type(d_type) == int:
		if d_type < 100:
			return 'less than 100'
		else: 
			return 'more than 100'

	# determine if the input is a string then 
	# count the number of letters is the string

	else:
		if type(d_type) == str:
			count_words = len(d_type)
			return count_words

# print data_type(None)