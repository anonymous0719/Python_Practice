#Python Program to learn Inheritance in  classes
class Sedan:
    def length(self):
        print("More than Hatchback")

class Fiat(Sedan):
    pass

class HondaCity(Sedan):
    def honda(self):
        print("shiny black car")

car1 = Fiat()
car2 = HondaCity()
car1.length()
car2.honda()