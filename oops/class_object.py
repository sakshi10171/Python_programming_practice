# Class and Object example

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)

# object creation
s1 = Student(1, "Sakshi")
s1.display()
