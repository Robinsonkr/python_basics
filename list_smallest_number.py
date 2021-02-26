#smallest number from a list
# numbers = input("enter values by space ")
# numbers_spl = numbers.split()
def minlist(ele):
	minn = ele[0]

	for x in ele:
		if x < minn:
			minn = x
	return minn

numbers = [20,10,30,125] 
print(minlist(numbers))

"""

10

"""