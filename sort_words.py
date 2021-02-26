#Sort Words in Alphabetic Order

my_str = input("enter a string")

#breakdown the string into a list of words 
words = my_str.split() 
print(words)

words.sort()

for word in words:
	print(word)