#Make new fruits by sending two iterable objects into the function
def make_new_fruits(item1, item2):
	return item1 + item2

fruits1 = ("apple","banana","orange")

fruits2 = ("capsikm","potato","tomato")

x = list(map(make_new_fruits,fruits1,fruits2))

print(x)

"""
['applecapsikm', 'bananapotato', 'orangetomato']

"""
