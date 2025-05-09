class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def enter_details(self):
        self.name = input("What is the name: ")
        self.age = input("How old is the person: ")
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Student(Person):
    
    def __init__(self, name, age, student_id, section):
        super().__init__(name, age)
        self.student_id = student_id
        self.section = section
        
    def enter_details(self):
        super().enter_details()
        self.student_id = input("What is the student ID: ")
        self.section = input("What is the section of the student: ")
        
    def display_details(self):
        super().display_details()
        print(f"Student ID: {self.student_id}")
        print(f"Section: {self.section}")
        
s = Student("", "", "", "")

s.enter_details()
s.display_details()
