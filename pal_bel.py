input_data = input("enter string or integer ")

def check_palindrome(ip):
	if(ip==ip[::-1]):
		print("palindrone")
	else:
		print("not palindrone")

try:
	if(type(eval(input_data))==int):
		check_palindrome(input_data)
	else:
		print("Enter valid number")
except NameError:
	check_palindrome(input_data)

except SyntaxError:
	print("enter valid")