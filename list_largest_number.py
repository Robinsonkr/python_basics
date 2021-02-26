# numbers = input("enter values by space ")
# numbers_spl = numbers.split()
def maxlist(ele):
	maxx = ele[0]

	for x in ele:
		if x > maxx:
			maxx = x
	return maxx

numbers = [10,20,30,10,125] 
print(maxlist(numbers))

"""

125

"""