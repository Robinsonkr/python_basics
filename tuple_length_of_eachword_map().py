#Calculate the length of each word in the tuple
#using map() and userdefined()
def length_of_each_word(item):
	return len(item)

my_tuple=("apple","banana","orange")

#convert the map into a list, for readability
x = list(map(length_of_each_word,my_tuple))

print(x)


"""
[5, 6, 6]

"""

