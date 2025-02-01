import pickle

class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

#Serialization
e = Employee("Anshika","Shrivansh")
f = open("D://Anshika//Python//Serialization.txt","wb")
pickle.dump(e, f)
f.close()
print("Done succesfully")

#Deserialization
f=open("D://Anshika//Python//Serialization.txt","rb")
e = pickle.load(f)
print(e.fname)
print(e.lname)