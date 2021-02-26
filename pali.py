


def checkpal(listt):
	if listt == listt[::-1]:
		print("palindrome")

	else:
		print("not palindrome")

strings = input("enter words using space ")
split_strings= strings.split()

checkpal(split_strings)