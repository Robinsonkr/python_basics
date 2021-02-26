def my_decorators(f):
	def wrapper():
		print("inside of the decorator before calling the function")
		f()
		print("inside of the decorator after calling the function")
	return wrapper


@my_decorators
def printname():
	print("iam robin")

printname()