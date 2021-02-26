#Converting Two Lists of the Same Length to a Dictionary
list1=[1,2,3,4]
list2=['a','b','c','d']

dict1 = zip(list1,list2)

print(dict(dict1))