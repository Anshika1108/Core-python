class Person:

    def __init__(self, Name, Age, Place):
        self.name = Name
        self.age = Age
        self.place = Place

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getPlace(self):
        return self.place


p = Person("Anshika", 21, "Indore")
print(p.getName())
print(p.getAge())
print(p.getPlace())