class Student: #class
	def __init__(self,name,mark1,mark2): #constructor
		self.name = name  #property1
		self.mark1 = mark1 #property2
		self.mark2 = mark2 #property3

	def total(self): #function
		return self.mark1 + self.mark2

	def avg(self): #another function
		return self.total()/2

	def display(self): #another function
		print(self.name)
		print(self.mark1)
		print(self.mark2)
		print("total is",self.total()) #calling total()
		print("avg is",self.avg()) #calling avg()

s1 = Student("Arun",80,90)
s1.display() #calling display()
s1.total() #calling total() 
s1.avg()  #calling avg()


s2 = Student("Binu",40,50)
s2.display()
s2.total()
s2.avg()





