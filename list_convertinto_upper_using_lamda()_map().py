#upper case the values in list
# use of lambda() function 
# with map() function 
fruits =["apple","orange","banana"]

uppered_fruits = list(map(lambda fruit:str.upper(fruit),fruits))
print(uppered_fruits)

"""
['APPLE', 'ORANGE', 'BANANA']

"""
