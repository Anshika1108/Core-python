class Person:
    count = 0

    def __init__(self):
        self.name = ""
        Person.count += 1

    def setName(self,n):
        self.name = n

    def getName(self):
        return self.name

p1 = Person()
p1.setName("Anshika")
p2 = Person()
p2.setName("Anshi")

print(p1.name)
print(p1.getName())
print(p2.getName())
print(Person.count)