#To change the value of a global variable inside a function, refer to the variable by using the global keyword

x = "awesome"  #global varaiable

def myfun():
	global x
	x = "fantastic"   #local variable into global variable(value changed)
	print(x)



myfun()
print(x)