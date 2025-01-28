a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
try:
    c = a/b
    print(c)
except Exception:
    print("check your division is zero")
finally:
    print("Always executed")

print("Hello World")