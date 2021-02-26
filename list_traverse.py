fruits = ["apple","banana","carrot","dalda","elephant"]

 # start at index 1 (included) and end at index 3 (not included)
new_list = fruits[1:3]
print(new_list)
"""
['banana', 'carrot']

"""

#range will start at the first item
print(fruits[:4])
"""
['apple', 'banana', 'carrot', 'dalda']

"""

#range will go on to the end of the list from 2nd index
print(fruits[2:])

"""
['carrot', 'dalda', 'elephant']

"""

#items from "banana" (-4) to, but NOT including "elephant" (-1)
print(fruits[-4:-1])
"""
['banana', 'carrot', 'dalda']

"""

#to print elements from end (-1 ) not included
print(fruits[:-1])

#list in revere order

print(fruits[::-1])



#['elephant', 'dalda', 'carrot', 'banana', 'apple']
