file =  open("D://Anshika//Python//Test.txt","w")
file.write("Hello world \n")
file.write("This is python file \n")
file.close()

file = open("D://Anshika//Python//Test.txt","r")
text = file.read()
print(text)
file.close()