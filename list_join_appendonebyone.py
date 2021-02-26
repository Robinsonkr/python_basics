#appending all the items from list2 into list1, one by one
list1 = ["apple","banana","carrot"]

list2 = [10,20,30]

for x in list2:
	list1.append(x)

print(list1)


"""
['apple', 'banana', 'carrot', 10, 20, 30]

"""