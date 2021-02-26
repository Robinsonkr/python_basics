#global keyword It convert the local variable inside the function into global variable


def myfun():
	global x
	x = "fantastic"   #local variable into global variable
	print(x)



myfun()
print(x)