# Only accept items that are not "apple"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = []

for x in fruits:
	if x!= "apple":
		new_list.append(x)

print(new_list)

"""
['banana', 'cherry', 'kiwi', 'mango']

"""