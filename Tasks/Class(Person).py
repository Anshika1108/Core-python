from datetime import datetime
# def calculate_age(DOB):
#     today = datetime.today()
#     age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))
#     return age
#
# dob = datetime(2003, 8, 11)
# age = calculate_age(dob)
# print(age)

class Person:

    name = None

    def setName(self,name):
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


p = Person()
p.setName("Anshika")
print("Name : ",p.getName())
print("Today date : ",p.Today())
print("DOB : ",p.Dob())
print("Age : ",p.Age())

