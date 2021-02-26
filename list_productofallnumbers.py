#numbers = input("Enter list elements seperated by space ")
# numbers_split = numbers.split()
#mul = mul * int(x)

def multiplies_list(items):
	mul = 1

	for x in items:
		mul = mul * x

	return mul

numbers = [10,20,30]
print(multiplies_list(numbers))


"""

6000

"""