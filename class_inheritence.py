#parent class
class Person:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def address(self):
        print(self.name, self.contact)

#child class1
class Doctor(Person):
    pass

#child class2
class Patient(Person):
    pass

#person object
per1 = Person("pervidu",852741)
per1.address()

#doctor object
doc1 = Doctor("Drjohn",123456)
doc1.address()

#patient object
pat1 = Patient("PatAnoop",987654)
pat1.address()
