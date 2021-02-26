#count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
def string_length(items):
	ctr= 0
	for x in items:
		if len(x) > 1 and x[0] == x[-1]:
			ctr += 1

	return ctr


list1=["apple","ab","usu",'abb']

print(string_length(list1))

"""
1

"""
