#Raise a TypeError if x is not an integer
x = "Hello"

if not type(x) is int:
    raise TypeError("Only integer allows")
