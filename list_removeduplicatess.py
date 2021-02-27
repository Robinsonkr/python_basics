def unique_list(list1):
	unique_listt =[]
	for i in list1:
		if i not in unique_listt:
			unique_listt.append(i)

	return unique_listt

my_list = [1, 3, 5, 6, 3, 5, 6, 1]


result = unique_list(my_list)
print(result)

"""
[1, 3, 5, 6]

"""