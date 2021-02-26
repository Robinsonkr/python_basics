#Requirement a person should be able to drive a car
#cars person
from abc import ABC,abstractmethod
class Car(ABC):   #abstract base class
	@abstractmethod
	def start(self):
		pass
	@abstractmethod
	def accelerate(self):
		pass
	@abstractmethod
	def stop(self):
		pass

class NanoCar(Car):
	def start(self):
		print("start nano car")
	def accelerate(self):
		print("accelerate nano car")

	def stop(self):
		print("stop benz car")
class BenzCar(Car):
	def start(self):
		print("start benz car")
	def accelerate(self):
		print("accelerate nano car")

	def stop(self):
		print("stop benz car")

class Person:
	def drive(self,car):
		car.start()
		car.accelerate()
		car.stop()

def main():
	car1 = NanoCar()
	car2 = BenzCar()

	person1 = Person()

	person1.drive(car1)
	person1.drive(car2)

main()