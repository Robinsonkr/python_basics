#list
#Ordered
#Indexed
#Changeable(mutable)
# Allows duplicate

fruits = ['apple', 'banana', 'cherry']
print(fruits)
fr = fruits

new_list = list(fruits)
print(id(fruits))
print(id(fr))
print(id(new_list))
print(dir(fruits))

"""
['apple', 'banana', 'cherry']

"""