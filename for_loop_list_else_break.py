#else block will NOT be executed if the loop is stopped by a break statement.
fruits = ["apple","banana","carrot"]

for i in fruits:
	if i == "banana":
		break
	print(i)

else:
	print("Finally finished")


"""
output
-------
apple

"""