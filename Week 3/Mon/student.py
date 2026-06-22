# Create a class Student
class Student:

    # define a class atrribute
    name = "John"
    nationality = "Ugandan"

    # Using the init
    def __init__(self, age, religion):
        self.age = age
        self.religion = religion


def print_name(self):
    print(f"Your name is {self.name}")
    qualities(self)


def qualities(self):
    print(f"You are a {self.nationality} {self.religion}")


student1 = Student(20, "Catholic")

print_name(student1)


print(student1.age)

()
