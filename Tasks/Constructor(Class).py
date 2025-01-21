from datetime import datetime
class Person:

    def __init__(self,name):
        self.name = name

    def Today(self):
        return datetime.today()

    def Dob(self):
        return datetime(2003, 8, 11)

    def Age(self):
        dob = datetime(2003, 8, 11)
        today = datetime.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def getName(self):
        return self.name


p = Person("Anshi")
print("Name : ",p.getName())
print("Today date : ",p.Today())
print("DOB : ",p.Dob())
print("Age : ",p.Age())