class Parent:

    def House(self):
        print("Parent's House")

class FirstChild(Parent):
    pass

f = FirstChild()
f.House()