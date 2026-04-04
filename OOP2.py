#inheritance

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"hello my name is {self.name} and my age is {self.age}")
        
        
class Teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject =  subject
        
    def info(self):
        print(self.name,self.subject)

t1 = Teacher("nigga",100,"maths")
t1.introduce()
print(t1.subject)
t1.info()

class engineer(person):
    def __init__(self, name, age,department):
        super().__init__(name, age)
        self.department = department
    def work(self):
        print(f"{self.name} is working in {self.department}")

class EngTeacher(engineer):
    def __init__(self, name, age, department,subject):
        super().__init__(name, age, department)
        self.subject = subject
    def info(self):
        print(f"this person teaches {self.subject} and works in department {self.department} ")
        
eng1 = EngTeacher("abj", 18 , "coder", "maths")
eng1.info()