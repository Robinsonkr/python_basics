#multiple inheritence
#A single derived class may inherit from 2 or more base class

class Parent1:
	def funct1(self):
		print("this is first function")


class Parent2:
	def funct3(self):
		print("this is third function")


class Child(Parent1,Parent2):
	def funct2(self):
		print("this is second function")


obj = Child()
obj.funct1()
obj.funct2()
obj.funct3()