#Sort the list by the length of the values 

def myfun(ele):
	print(len(ele))
	return len(ele)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myfun)
print(cars)

"""

['VW', 'BMW', 'Ford', 'Mitsubishi']

"""