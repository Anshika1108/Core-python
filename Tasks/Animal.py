from abc import ABC, abstractmethod
class Animal():

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
          print("Bark")

class Cat(Animal):

    def speak(self):
        print("Meow")

D = Dog()
C = Cat()

for sounds in (D,C):
    sounds.speak()

