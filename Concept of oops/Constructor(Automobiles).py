class Automobiles :

    def __init__(self,color,speed,make):
        self.color = color
        self.speed = speed
        self.make = make

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    def getMake(self):
        return self.make

a = Automobiles("Black",150,"apache")
print(a.getColor())
print(a.getSpeed())
print(a.getMake())