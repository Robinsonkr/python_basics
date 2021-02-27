#print the even numbers from a given list.
def get_even(list1):
	even_list = []

	for i in list1:
		if i % 2 == 0:
			even_list.append(i)

	return even_list


my_list = [2,1,3,5,8,6,4]

result = get_even(my_list)

print(result)

"""
[2, 8, 6, 4]


"""