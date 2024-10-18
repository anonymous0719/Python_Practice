#Python Program to learn Inheritance in  classes
class Sedan:
    def length(self):
        print("More than Hatchback")

class fiat(Sedan):
    pass

class hondaCity(Sedan):
    def honda(self):
        print("shiny black car")

car1 = fiat()
car2 = hondaCity()
car1.length()
car2.honda()
