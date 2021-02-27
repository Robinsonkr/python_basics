# we have created a whole new object for list1
#we try to change the reference(ie, list1) that was passed in as a parameter
#not affected the original object
fruits = ["apple","banana","orange"]

def my_function(list1):
	list1 = ["guava","pineapple","grape"]
	return list1


x= my_function(fruits)

print("inside function result is", x)

print("outside function result is", fruits)

"""
inside function result is ['guava', 'pineapple', 'grape']
outside function result is ['apple', 'banana', 'orange']


"""

