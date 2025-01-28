a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
try:
    c = a/b
    print(c)
except ZeroDivisionError :
    print("check your division is zero")
else:
    print("your division was greater than zero")