from collections import OrderedDict
my_list = [2,5,4,8,10,10]
unique_list= list(OrderedDict.fromkeys(my_list))
print(unique_list)

"""
[2, 5, 4, 8, 10]

"""

