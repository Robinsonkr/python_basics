def my_decorators(f):
	def wrapper(*args, **kwargs):
		print("inside of the decorator before calling the function")
		f(*args, **kwargs)
		print("inside of the decorator after calling the function")
	return wrapper


@my_decorators
def printname(name):
	print(name)

printname("Robin") 