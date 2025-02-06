a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

try :
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero error")
except TypeError :
    print("type error")

