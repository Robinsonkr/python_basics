# Arguments in Python Passed by Reference
#changes made within a function are reflected in the original object
fruits =["apple","banana","carrot"]

def my_function(list1):
	list1[0] = "guava"
	return list1




result = my_function(fruits)
print("inside the function result ", result)

print("outside the function ", fruits)


"""
inside the function result  ['guava', 'banana', 'carrot']
outside the function ['guava', 'banana', 'carrot']



"""