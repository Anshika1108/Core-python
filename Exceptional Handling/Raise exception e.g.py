number = int(input("Enter the Number :"))

try:
    if number<10 :
        raise Exception("Value is too small")
    else:
        print(number)
except Exception as e:
    print(e)