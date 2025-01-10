# First Function
def hello():
    print("hello anshika")
hello() #this is used to call the above function

def my_function():
     print("hello my 1st function")
my_function()

# Parameter Function
def my_function(fname):
    print(fname + " gupta")
def my(name):
    print(name + " Shrivansh")

my("Anshika")
my_function("aniket")
my_function("Ram")

# Set Value as a Parameter
country_name = input("Enter your Country Name :")
def my_function(country=country_name):
    print("I am From " + country)
my_function()

# Parsing List as a Parameter
def my_function(food):
    for x in food:
        print(x)

fruits = ["appple","bnana","pineapple"]

print(fruits)

my_function(fruits)


# Return Value as a Parameter
def mul(h):
    return 5 * h
print(mul(6))

def sum(a, b):
     return a + b
print(sum(20,30))

def div(c,d):
    return c/d
print(div(20,2))

def sub(x,y):
    return x-y
print(sub(75,50))
