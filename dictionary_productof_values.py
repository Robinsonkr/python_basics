#product of all numbers stored in a dictionary
#user defined function
def productofdictionary(items):
	mul = 1
	for x in items:
		mul = mul * items[x]
	return mul

numbers = {'a': 100, 'b':200, 'c':300} 

print(productofdictionary(numbers))

"""

6000000

"""