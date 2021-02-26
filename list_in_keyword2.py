#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = []

for x in fruits:
	if "a" in x:
		new_list.append(x)

print(new_list)


"""
['apple', 'banana', 'mango']

"""