#square of numbers between 1 and 10 (both included) using range
def get_squares():

	squares_list = []

	for i in range(1,11):
		squares_list.append(i**2)

	return squares_list

result = get_squares()
print(result)

"""
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""