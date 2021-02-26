#tupleinto dictionary with reverse key
tuple1= ((5,"apple"),(10,"banana"))

dict1= dict((y,x) for (x,y) in tuple1)

print(dict1)
print(type(dict1))

"""
{'apple': 5, 'banana': 10}
<class 'dict'>

"""