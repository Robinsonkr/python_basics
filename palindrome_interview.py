string=input(("Enter a string: "))
rev_string = string[::-1]
if string == rev_string:
	print("The string is a palindrome")
else:
	print("Not a palindrome")