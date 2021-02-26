class Sample: #class
	text = "Hello World" #global variable
	def __init__(self):
		print("This is my first class")

	def funct1(self):
		print("value of text",self.text)


s1 = Sample() #object1
s1.funct1() #calling funct1
