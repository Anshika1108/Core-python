class Grandparent():

    def Property(self):
        print("Grand Parent's Property")

class Parent():

    def House(self):
        print("Parent's House")

class Child(Grandparent,Parent):

    def Child(self):
        Grandparent.Property()
        Parent.House()

c = Child()
c.House()
c.Property()



