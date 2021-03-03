# Python program to find the factorial of a number or (user input)
"""
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720

#n! = n *(n-1) * (n-2) *... *1
"""
class Fact:
	def __init__(self,num):
		self.number = num

	def factorial(self):
		factorial = 1
		if self.number < 0:
			print("doesnot exist for negetive number")

		elif self.number == 0:
			print("0 factorial is 1")

		else:
			for i in range(1,self.number +1): 
				factorial = factorial * i

			return factorial

numb = Fact(5)
result = numb.factorial()
print(result)

"""
120

"""
