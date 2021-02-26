#sum of all integers stored in a list (user input)
#user defined function
def sumoflist(items):
	summ = 0
	for x in items:
		summ = summ + int(x)
	return summ

numbers = input("Enter list elements seperated by space(default): ")
#split(',') or split(' ')
numbers_split = numbers.split()

print(sumoflist(numbers_split))

"""
Enter list elements seperated by space: 25 25

50

"""
