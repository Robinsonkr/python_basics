#only divisible by 1 and itself
#2 3 5 7 11
#5 ie, 5 * 1 or 1 * 5

#prime number or not

num = int(input("Enter a number "))
if num > 1:
	for x in range(2,num):
		if(num%x)==0:
			print("Not Prime")
			# print(x,"times",num//x,"is",num)
			break
	else:
		print(num," is a prime number")
	
else:
	print(num ," is not a prime number")