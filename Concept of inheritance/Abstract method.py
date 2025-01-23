from abc import ABC,abstractmethod

class Shape():
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b

class Circle(Shape):

    def __init__(self,r):
        self.r = r

    def area(self):
        return self.r*2

class Triangle(Shape):

    def __init__(self,b,h):
        self.b = b
        self.h = h

    def area(self):
        return self.b*self.h/2

R = Rectangle(20,30)
C = Circle(10)
T = Triangle(30,15)
print(R.area())
print(C.area())
print(T.area())
S = Shape()
print(S.area())