#single inheritance
#One derived class inherits one base class

class Parent:
	def funct1(self):
		print("this is a parent function")

class Child(Parent):
	def funct2(self):
		print("this is a child function")


obj = Child()
obj.funct1()
obj.funct2()

