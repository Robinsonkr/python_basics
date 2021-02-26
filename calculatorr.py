from fun import *
print("Demo Calculator")
print("---------------")
print("options")
print("-------")

print("1 for addition")
print("2 for multiplication")
print("3 for subtraction")
print("4 for division")

number = int(input("what you want to do? "))
a = int(input("enter first number "))
b = int(input("enter second number "))

if number == 1:
	addition(a,b)
	# print(a+b)
elif number == 2:
	multiplication(a,b)
elif number == 3:
	subtraction(a,b)
elif number == 4:
	division(a,b)
else:
	print("Invalid")