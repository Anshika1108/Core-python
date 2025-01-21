import datetime
class Person:
    # Class-level attributes
    name = None
    DOB = None
    age = None
    address = None

    def setName(self, name):
        self.name = name

    def setDOB(self, DOB):
        self.DOB = DOB

    def setage(self, age):
        self.age = age

    def setaddress(self, address):
        self.address = address

    def getName(self):
        return self.name

    def getDOB(self):
        return self.DOB

    def getage(self):
        return self.age

    def getaddress(self):
        return self.address

p = Person()
p.setName("Anshika")
p.setDOB(datetime.datetime(2003,8,11))
p.setage(21)
p.setaddress("Indore")
print(p.getName())
print(p.getDOB())
print(p.getage())
print(p.getaddress())