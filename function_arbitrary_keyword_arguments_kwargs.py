def myfunction(**names):
	print("Hello", names["fname"])
	# print("Hello " , names)

myfunction(fname="Robin",lname="kr")

"""
Hello Robin
# Hello  {'fname': 'Robin', 'lname': 'kr'}

"""