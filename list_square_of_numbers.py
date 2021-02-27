def get_squares(list1):

	squares_list = []

	for i in list1:
		squares_list.append(i**2)

	return squares_list

my_list=[1,2,3,4,5,6,7,8,9,10]
result = get_squares(my_list)
print(result)