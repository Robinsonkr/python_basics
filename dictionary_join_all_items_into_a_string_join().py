#When using a dictionary as an iterable,
#the returned values are the keys, not the values
#Join all items in a dictionary into a string, using a the word "TEST" as separator:
# If the key of the string is not a string, it raises a TypeError exception
my_dictionary = {"name": "Robin","place":"Alappuzha"}
mySeparator = "TEST"

x = " ".join(my_dictionary)
print(x)

x = mySeparator.join(my_dictionary)
print(x)

"""
name place
nameTESTplace

"""