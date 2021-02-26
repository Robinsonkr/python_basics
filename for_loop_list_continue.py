#Do not print banana
fruits = ["apple","banana","carrot"]

for i in fruits:
	if i == "banana":
		continue
	print(i)

"""
output
------
apple
carrot

"""