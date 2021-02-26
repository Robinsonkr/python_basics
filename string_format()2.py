#format() method to insert numbers into strings with multiple argument
quantity = 3
itemno = 567
price = 49.95

myorder = "i want {} quantity with {} itemno for {} price"

print(myorder.format(quantity,itemno,price))