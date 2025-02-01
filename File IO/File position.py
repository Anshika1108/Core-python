with open ("File position.txt","w") as file :
    file.write("HelloWorld \n")

file = open("File position.txt")
str = file.read(10)
position = file.tell()
position = file.seek(0,0)
print(position)
print(str)
