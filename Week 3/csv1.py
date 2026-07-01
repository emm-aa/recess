import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open("students.csv", "a", newline="\n") as file:
    fieldnames = ["Reg No", "Name", "Gender", "Age", "Course", "Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if file.tell() == 0:
        writer.writeheader()

    new_student = {
        "Reg No": "24U002",
        "Name": "Arinda",
        "Gender": "Male",
        "Age": 20,
        "Course": "Computer Science",
        "Score": 85,
    }
    writer.writerow(new_student)

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
