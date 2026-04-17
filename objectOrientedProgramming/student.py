class Student:

    def __init__(self,rol,name,age,course):

        self.rol = rol

        self.name = name

        self.age = age

        self.course = course

    def display_student(self):

        print(self.rol,self.name,self.course,self.age)

student_instance = Student(123,"vipin",24,"bsccs")

student_instance.display_student()


# oop features
# inheritance
# polymorphism
# abstraction
