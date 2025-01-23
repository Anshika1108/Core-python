class Vehicle():
    
    def move(self):
        print("Vehicle is moving")
        
class Car(Vehicle):

        def move(self):
            print("Car is moving")
            super().move()

c = Car()
c.move()
        
            
