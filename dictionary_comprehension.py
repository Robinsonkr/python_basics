#Based on a dict of fruits, you want a new dict, containing only the fruits with the letter "a" in the name
fruits = {"apple":1, "banana":20, "cherry":30}
new_dict = [x for x in fruits if "a" in x]

print(new_dict)

"""
['apple', 'banana']

"""