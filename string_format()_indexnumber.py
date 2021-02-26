#format() with index numberto insert numbers into strings with multiple argument
##numbered indexes:
quantity = 3
itemno = 567
price = 49.95

myorder = "i want {0} quantity with {1} itemno for {2} price"

a = myorder.format(quantity,itemno,price)

print(a)