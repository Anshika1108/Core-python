class Parent:

    def Money(self):
        print("parent's money")

class Child(Parent):
    pass

c = Child()
c.Money()