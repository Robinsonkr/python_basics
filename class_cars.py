#property- name,price,colour ,method- start()
class Cars:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def start(self):
        print(self.name + " Engine started")

car1 = Cars("Maruthi Swift", 10000, "Red")
car2 = Cars("Toyoto innova", 20000, "white")
# del car1.color #delete color attribute
# del car2 #delete car2 object
# car1.price = 15000  #modify attribute

car1.start()
car2.start()
print(car1.name, car1.price, car1.color)
print(car2.name, car2.price, car2.color)