#join() method takes all items in an iterable and joins them into one string
myTuple = ("My","Name","is","John")

x = "".join(myTuple)
print(x)
x = "#".join(myTuple)
print(x)
x = " ".join(myTuple)
print(x)
x=', '.join(myTuple)
print(x)

# .join() with tuples
numTuple = ('1', '2', '3', '4')

"""
MyNameisJohn

My#Name#is#John

My Name is John

My, Name, is, John

"""