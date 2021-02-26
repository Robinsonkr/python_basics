#reverse a list using function (slicing technique)
def my_function(lst):
  return [ele for ele in reversed(lst)] 

my_list= [10, 11, 12, 13, 14, 15]
print(my_function(my_list))

"""
[15, 14, 13, 12, 11, 10]

"""