# Polymorphism example

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barking")

a = Dog()
a.sound()
