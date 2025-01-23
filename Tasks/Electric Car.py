class Car():

    make = None
    model = None
    year = None

    def setDescription(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

class Electric_Car(Car):
    def setBattery_capacity(self, battery):
        self.battery = battery

    def getBattery_capacity(self):
        return self.battery





E = Electric_Car()
E.setDescription("Tata","Nexon EV",2020)
E.setBattery_capacity("30.2 kWh")
print("# Electric car Description")
print("Make :",E.make)
print("Model :",E.model)
print("Year :",E.year)
print("Battery Capacity :",E.getBattery_capacity())
