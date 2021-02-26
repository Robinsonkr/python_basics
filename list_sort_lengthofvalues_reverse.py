#Sort the list by the length of the values (reverse=True)
def myfun(ele):
	return len(ele)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True,key=myfun)
print(cars)

"""

['Mitsubishi', 'Ford', 'BMW', 'VW']

"""