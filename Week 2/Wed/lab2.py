import math

# def area(l, w):
#     num = l * w
#     print(f"The area is {num} units")


# print(f"Enter rectangle to calculate.")
# length = int(input("Length: "))
# width = int(input("Width: "))

# area(length, width)

# Return statements send value back to caller

# Parameters are variables listed in a function
# during its definition.

# Arguments are the actual values that are
# passed to a function when it is being used.


# def display_info(n, s, a, c, year="2026"):
#     print(f"Student's name is {n}, studentNumber:{s}")
#     print(f"They are doing a course in {c}.")
#     print(f"They are {a} years of age in {year}.")
#     return 0


# name = input("Enter details...\nName: ")
# student_number = int(input("Student Number: "))
# age = int(input("Age: "))
# course = input("Course: ")
# print()

# display_info(course, a=age, s=student_number, c=course)


# def add(a, b):
#     print(a + b)
#     return a + b + a


# def multiply(a, b):
#     return a * b
#     print(a * b)


# add(2, 3)
# print(add(2, 3))

# print(multiply(2, 3))


def circle_area(radius):
    area = math.pi * radius * radius
    return area


print(f"The area of circle with radius 5 is {circle_area(5):.2f} units")
print()

# Global var
variable = "Global"


# Local var
def function():
    variable = "Variable"
    print(variable + " inside local function")


print(variable)
function()
print(variable)
