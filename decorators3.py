#Pretty Printed youtube channel
def my_decorators(msg="Message"):

	def decorated(f):
		def wrapper(*args, **kwargs):
			print("the msg is ",msg)
			print("inside of the decorator before calling the function")
			f(*args, **kwargs)
			print("inside of the decorator after calling the function")
		return wrapper
	return decorated


@my_decorators(msg="Hello")
def printname(name):
	print(name)

printname("sara")