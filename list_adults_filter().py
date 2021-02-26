# Filter the array, and return a new array with only the values equal to or above 18
ages = [11,15,18,25,30]

def get_adults(item):
	if item < 18:
		return False

	else:
		return True

adults = filter(get_adults,ages)

for x in adults:
	print(x)

"""
18
25
30

"""

