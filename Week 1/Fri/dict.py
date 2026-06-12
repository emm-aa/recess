score = dict([("math", 90), ("english", 85), ("science", 95)])
print(type(score))

# Updating value
score["english"] = 88
# # score["physics"] = 92

# # Iterating through a dictionary
for subject in score.keys():
    print(subject)
for mark in score.values():
    print(mark)
for subject, mark in score.items():
    print(f"{subject.title()} has {mark}")

# # adding a new subject
# score["history"] = 80
# print(score)

# # List dictionary operations
subjects = ["math", "english", "science"]
marks = [90, 85, 95]
score = dict(zip(subjects, marks))
print(score)

# print(score.get("math"))

# Nested dictionary
students = {
    "John": {"math": 90, "english": 85, "science": 95},
    "Arinda": {"math": 80, "english": 88, "science": 92},
    "Moses": {"math": 85, "english": 90, "science": 88},
}

for student, subjects in students.items():
    print(f"{student} has the following scores:")
    for subject, mark in subjects.items():
        print(f"  {subject.title()}: {mark}")
