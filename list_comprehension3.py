# Only accept items that are not "apple" using list comphrehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if x!= "apple"]

print(new_list)

"""
['banana', 'cherry', 'kiwi', 'mango']

"""