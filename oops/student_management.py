# Student Management using OOP

class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Marks:", self.marks)

    def is_pass(self):
        if self.marks >= 40:
            print("Status: Pass")
        else:
            print("Status: Fail")


# creating objects
s1 = Student(1, "Sakshi", 22)
s2 = Student(2, "Rashi", 23)

s1.display()
s1.is_pass()

print()

s2.display()
s2.is_pass()
