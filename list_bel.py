list_of_words = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
result=list()
def check_pali(data):
	if(data==data[::-1]):
		result.append(data)
	else:
		print(data + "is not palindrome")

for data in list_of_words:
	check_pali(data)

print(result)
