class Bike():

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

b = Bike()
b.setDescription("Pulsar","NS125",2024)
print("Make :",b.make)
print("Model :",b.model)
print("Year :",b.year)
