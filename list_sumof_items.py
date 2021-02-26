#sum of all numbers stored in a list
#user defined function
def sumoflist(items):
	summ = 0
	for x in items:
		summ = summ + x
	return summ

numbers = [10,20,30]
# print(sum(numbers)) #builtin

print(sumoflist(numbers))

"""

60

"""
