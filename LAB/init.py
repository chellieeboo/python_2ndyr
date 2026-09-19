#Checked
class Student:
    def __init__(self, name, age, id, program, school, course):
        self.name = name
        self.age = age
        self.id = id
        self.program = program
        self.school = school
        self.course = course

    def greet(self):
        print(f"Good day everyone I'm {self.name}, and I am {self.age} my student id is {self.id}, "
              f"currently I'm taking course {self.program}, at {self.school} in this course {self.course}.")


my_info = Student(
    "Rochelle",
    20,
    6362,
    "Bachelor of Science in Information Technology",  
    "Northern Luzon Advcentist College",                          
    "DSA"                                             
)

my_info.greet()