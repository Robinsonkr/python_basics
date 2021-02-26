# Python program to find the factorial of a number or (user input)
"""
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720

#n! = n *(n-1) * (n-2) *... *1
"""
def factorial(num):
	factorial = 1
	if num < 0:
		print("doesnot exist for negetive number")

	elif num == 0:
		print("0 factorial is 1")

	else:
		for i in range(1,num +1): 
			factorial = factorial * i

		return factorial

num = 1
print(factorial(num))