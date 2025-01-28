try:
    d=int(input("Enter value:"))
    a='10'
    b='a'
    c=a/b
    print(c)
    print(d)
except TypeError :
    print("type error")
except ValueError:
    print("value error")
except ModuleNotFoundError :
    print("module not found")