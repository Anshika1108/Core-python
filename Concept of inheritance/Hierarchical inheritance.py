class Parent:

    def House(self):
        print("Parent's House")

class FirstChild(Parent):
    pass

class SecondChild(Parent):

    def Bike(self):
        print("Bike")

s = SecondChild()
s.House()
s.Bike()






