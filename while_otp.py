#write a program to check the otp
otp = 2325

attempt = 0

while attempt <3:
	user_otp = int(input("enter otp "))
	attempt+=1
	if user_otp == otp:
		print("correct otp")
		break

else:
	print("account blocked")
