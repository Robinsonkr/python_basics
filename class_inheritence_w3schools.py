class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname ,self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self,fname,lname)
        self.graduationyear = year


    def welcome(self):
        print(self.firstname,self.lastname,self.graduationyear)

#person object
# per1 = Person("Robinson", "Robert")
# per1.printname()


#student object
stu1 = Student("Anoop","TD",2018)
stu1.welcome()