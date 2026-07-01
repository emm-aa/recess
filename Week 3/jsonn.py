# Writing a JSON file
# import json

# student = {"name": "Joshua", "Age": "22", "Course": "Python"}

# with open("student.json", "a") as file:
#     json.dump(student, file, indent=4)


# Exercise 3: Write a custom exception for a Ugandan to drive a car, "Must be 18 years or older" using try and except block
class AgeException(Exception):
    pass


age = int(input("Enter your age: "))
# use in a try catch block
try:
    if age < 18:
        raise AgeException("Must be 18 years or older to drive a car.")
    else:
        print("You are eligible to drive a car.")
except AgeException as e:
    print(e)
