# numbers = input("enter values by space ")
# numbers_spl = numbers.split()

numbers = [10,20,30,5,125] 


def minlist(ele):
	minn = ele[0]

	for x in ele:
		if x < minn:
			minn = x
	return minn

print(minlist(numbers))

"""
5

"""