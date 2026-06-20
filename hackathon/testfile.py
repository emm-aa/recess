# Student grade manager
# Processes a list of students and their scores

studentList = []
MaxScore = 100
passing_threshold = 50


def addStudent(Name, score):
    """
    Adds a student and their score to the list.
    Only adds if the score is within valid range.
    """
    if score < 0 or score > MaxScore:
        print("Invalid score")
        return

    student_entry = {"name": Name, "score": score}
    studentList.append(student_entry)


def computeAverage(students):
    total = 0
    Count = 0

    for student in students:
        total += student["score"]
        Count += 1

    if Count == 0:
        return 0

    return total / Count


def getGrade(score):
    if score >= 80:
        return "A"
    elif score >= 65:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def printResults(students):
    avg = computeAverage(students)
    print(f"Average score: {avg:.2f}")

    for student in students:
        grade = getGrade(student["score"])
        status = "PASS" if student["score"] >= passing_threshold else "FAIL"
        print(f"{student['name']}: {student['score']} -> {grade} ({status})")


addStudent("Alice", 82)
addStudent("Bob", 47)
addStudent("charlie", 91)
addStudent("Diana", 65)
addStudent("eve", 30)

printResults(studentList)
