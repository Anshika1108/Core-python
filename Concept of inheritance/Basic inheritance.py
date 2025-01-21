class Shape :
    def __init__(self,color,borderwidth):
        self.color = color
        self.borderwidth = borderwidth

    def getColor(self):
        return self.color

    def getBoderwidth(self):
        return self.borderwidth

# s = Shape("Black",3)
# print(s.color)
# print(s.borderwidth)

class Reactangle(Shape):

    def __init__(self,lenght,width,color,borderwidth):
        super().__init__(color,borderwidth)
        self.lenght = lenght
        self.width = width

    def getLenght(self):
        return self.lenght

    def getWidth(self):
        return self.width

    def Area(self):
        return self.lenght*self.width

r = Reactangle(10,15,"blue",5)
print("Rectangle color :",r.getColor())
print("Area of rectangle :",r.Area())

class Circle(Shape):

    Pie = 3.14

    def __init__(self, radius, color, borderwidth):
        super().__init__(color, borderwidth)
        self.radius = radius

    def getRadius(self):
        return self.radius
    def AreaofCircle(self):
        return Circle.Pie*self.radius**2

c = Circle(5,"Red",8)
print("Circle color :",c.getColor())
print("Area of circle :",c.AreaofCircle())

class Triangle(Shape):

    def __init__(self,base,height,color,borderwidth):
        # super().__init__(color,borderwidth) or Person.__init__(self,color,borderwidth)
        super().__init__(color,borderwidth)
        self.base = base
        self.height = height

    def getBase(self):
        return self.base

    def getHeight(self):
        return self.height

    def AreaofTriangle(self):
        return self.base*self.height/2

t = Triangle(10,6,"Yellow",9)
print("Triangle color :",t.getColor())
print("Area of triangle :",t.AreaofTriangle())