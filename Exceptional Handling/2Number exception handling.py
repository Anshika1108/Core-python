try:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Non-numeric inputs provides")

