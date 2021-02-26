#convert into upper
#using map() and userdefied function
def list_to_upper(item):
	return item.upper()

fruits=['orange', 'grape', 'kiwi']

print(list(map(list_to_upper,fruits)))

