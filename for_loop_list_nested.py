#nested for loop
colors = ["red","orange","blue"]

fruits=["apple","banana","carrot"]

for i in range(len(colors)):
	for j in range(len(fruits)):
		print(i,j)

"""
output
-------
red apple
red banana
red carrot
orange apple
orange banana
orange carrot
blue apple
blue banana
blue carrot

"""