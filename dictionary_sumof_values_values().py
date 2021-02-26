#sum of all numbers stored in a list
#user defined function
def sumofdictionary(items):
	summ = 0
	for x in items.values():
		summ = summ + x
	return summ

numbers = {'a': 100, 'b':200, 'c':300} 

print(sumofdictionary(numbers))

"""

600

"""
