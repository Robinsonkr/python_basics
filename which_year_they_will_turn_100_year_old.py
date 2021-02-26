#which year they will turn 100 year old
def hundredyear(name,age,current_year):
	leftage = 100 - age
	year_of_hundred = current_year + leftage
	return year_of_hundred 
try:
	name = input("What is your name: ")
	age = int(input("How old are you: "))
	current_year = int(input("current year: "))

except ValueError:
	print("Enter integer only")

except:
	print("something went wrong")

print(hundredyear(name,age,current_year))



"""
or 
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)

"""