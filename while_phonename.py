#write a program to check the phone name
phone = "IPHONE"

attempt = 0

while attempt < 3:
	user_phone = str(input("enter correct phone name"))
	attempt +=1
	if user_phone == phone:
		print("correct")
		break

else:
	print("your chance are end")