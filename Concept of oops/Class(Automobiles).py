class Automobile:

    color = None
    speed = None
    make = None

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

a = Automobile()
a.setColor("Black")
a.setSpeed(120)
a.setMake("apache")
print("color",a.getColor())
print("speed",a.getSpeed())
print("make",a.getMake())