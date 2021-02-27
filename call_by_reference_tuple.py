fruits = ("apple","banana","orange")

def my_function(tuple1):
	tuple1 = tuple1 + ("grape",)
	return tuple1

result = my_function(fruits)

print("inside function result", result)
print("outside function ", fruits)

"""
inside function result ('apple', 'banana', 'orange', 'grape')
outside function  ('apple', 'banana', 'orange')

"""