file = open("using for loop.txt","w")
for i in range(5):
    file.write("hello world \n")
    file.write("This is python file \n")
file.close()

file = open("using for loop.txt","r")
read = file.read()
print(read)
file.close()
