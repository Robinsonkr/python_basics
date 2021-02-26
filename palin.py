def isPalindrome(s):
	return s == s[::-1]

try: 
	s = input("enter value to checkk ")
	ans = isPalindrome(s)
	if ans:
		print("palindrome")
	else:
		print("Not palindrome")

except ValueError:
	print ('That is not a valid number, Try Again !')

