#polymorphism

class Person:
    def introduce(self):
        print("I am Abdul Samad")
        
class Teacher(Person):
    def intoduce(self):
        print("I am Abdul Samad, a computer science teacher")

class Engineer(Person):
    def introduce(self):
        print("I am Abdul Samad, an electrical engineer")
        
class CSTeacher(Person):
    def introduce(self):
        print("I am Abdul Samad, and I am teaching OOP in Python")
        
people = [Person(), Teacher(), Engineer(), CSTeacher()]
for obj in people:
    obj.introduce()
    