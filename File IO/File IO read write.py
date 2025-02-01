file =  open("Test.txt","w")
file.write("Hii\n")
file.write("This is python file \n")
file.close()

file = open("Test.txt","r")
text = file.read()
print(text)
file.close()