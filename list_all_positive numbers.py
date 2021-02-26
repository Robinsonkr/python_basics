# all positive numbers from given list using for loop
my_list = [10,20,-5,5,-10,0]

positive_list=[]

for num in my_list:
	if num >= 0:
		# print(num, end=' ')
		positive_list.append(num)

print(positive_list)


"""
# 10 20 5 0
[10, 20, 5, 0]

"""

