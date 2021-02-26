class Person: #class
	def __init__(self,name,age): #constructor
		self.name = name #property 1
		self.age = age #property 2

	def Display(self): #function
		print("name is",self.name,"age",self.age)

p1= Person("Robin",12) #object1
del p1 #delete object
p1.Display() #calling display()
