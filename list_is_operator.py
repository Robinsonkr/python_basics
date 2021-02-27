#The ‘is’ operator compares the id of the two objects

list1 = ["apple","banana","orange"]

list2 = ['apple',"banana","orange"]

list3 = list1

print(list1 == list2)   #return TRUE  ,only values are same, id's are different

print(list1 is list2)   #return False ,only values are same, id's are different

print(list1 == list3)   #return TRUE  ,only values are same, id's are different

print(list1 is list3)   #return True, both values and id's are same