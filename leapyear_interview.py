 #leap year or not

year = int(input("Enter a year "))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("{0} is leap year".fomat(year))
		else:
			print("{0} is not a leap year".format(year))

	else:
		print("{0} is leap year".fomat(year))

else:
	print("{0} is not a leap year".fomat(year))
