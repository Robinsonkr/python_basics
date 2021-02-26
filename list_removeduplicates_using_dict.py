#Remove any duplicates from a List
mylist = ["apple","banana", "apple", "carrot", "carrot"]
unique_list = list(dict.fromkeys(mylist))

print(unique_list)


"""
['apple', 'banana', 'carrot']

"""