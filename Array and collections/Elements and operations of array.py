from  array import *
# Elements of array

# String
print("* String")
name = ['Anshi','Anshika','Jay']
x = name[1];
print(x)
print(name[0])

print("-----------------------------------------------------------------------------------------------")

#Integers
print("* Integers")
int = array("i",[10,20,30,40,50])
print(int[2])

print("-----------------------------------------------------------------------------------------------")

#Float
print("* Float")
float = array("f",[10.2,12.5,35.6,39.8])
print(float[3])

print("-----------------------------------------------------------------------------------------------")

#Lenght of array
print("* Lenght of array")
Names = ['Anshi','Anshika','Jay']
Integers = array("i",[10,20,30,40,50])

print(len(Names))
print(len(Integers))

print("-----------------------------------------------------------------------------------------------")

# Insert operation in array
print("* Insert operation in array")
Array1 = array("i",[10,20,30,40,50])
Array1.insert(1,70)
for x in Array1:
    print(x)

print("-----------------------------------------------------------------------------------------------")

# Delete operation in array
print("* Delete operation in array")
Array2 = array("i",[10,20,30,40,50])
Array2.remove(30)
for y in Array2:
    print(y)

print("-----------------------------------------------------------------------------------------------")

# Update operation
print("* Update operation")
Array3 = array("i",[10,20,30,40,50])
Array3[3] = 90
for x in Array3:
    print(x)