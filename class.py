class Sample:#class
	name = "Robin"  #proprty or attribute

	def greet(self):
		print('Hello')

# print(Sample.name)
obj = Sample() #object of sample class
print(obj.name)


#Call greet method
obj.greet()
