class Parent:

    def House(self):
        print("Parent's House")

class FirstChild(Parent):
    pass

class SecondChild(FirstChild):

    def Bike(self):
        print("Brother's Bike")



s = SecondChild()
s.House()
s.Bike()
