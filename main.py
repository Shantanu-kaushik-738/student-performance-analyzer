SUBJECTS = ["Python", "DBMS", "Statistics"]
PASS_MARKS = 33
MAX_MARKS_PER_SUBJECT = 100


students = [
    {"name": "Aman", "marks": [85, 78, 92]},
    {"name": "Priya", "marks": [95, 91, 89]},
    {"name": "Rahul", "marks": [32, 45, 28]},
    {"name": "Neha", "marks": [70, 80, 75]},
    {"name": "Rohit", "marks": [88, 76, 90]},
    {"name": "Anjali", "marks": [91, 94, 87]},
    {"name": "Vikas", "marks": [55, 62, 58]},
    {"name": "Sneha", "marks": [78, 85, 82]},
    {"name": "Karan", "marks": [29, 35, 40]},
    {"name": "Pooja", "marks": [96, 89, 98]},
]


def validate_marks(marks): 
    if not isinstance(marks, list) or not marks:
        raise ValueError("Marks must be a non-empty list.")

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise ValueError("Each mark must be a number.")
        if not 0 <= mark <= MAX_MARKS_PER_SUBJECT:
            raise ValueError(
                f"Each mark must be between 0 and {MAX_MARKS_PER_SUBJECT}."
            )


def validate_student(student, subject_count): 
    if not isinstance(student, dict):
        raise ValueError("Each student must be a dictionary.")
    if not isinstance(student.get("name"), str) or not student["name"].strip():
        raise ValueError("Each student must have a non-empty name.")

    marks = student.get("marks")
    validate_marks(marks)

    if len(marks) != subject_count:
        raise ValueError(
            f"{student['name']} must have marks for exactly "
            f"{subject_count} subjects."
        )


def calculate_total(marks): 
    validate_marks(marks)
    return sum(marks)


def calculate_percentage(marks): 
    validate_marks(marks)
    return calculate_total(marks) / len(marks)


def check_result(marks): 
    validate_marks(marks)
    return all(mark >= PASS_MARKS for mark in marks)


def calculate_grade(percentage): 
    if percentage >= 90:
        return "A"
    if percentage >= 75:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 33:
        return "D"
    return "F"


def analyze_student(student): 
    validate_student(student, len(student.get("marks", [])))
    marks = student["marks"]
    percentage = calculate_percentage(marks)
    passed = check_result(marks)

    return {
        "name": student["name"],
        "total": calculate_total(marks),
        "percentage": percentage,
        "result": "Pass" if passed else "Fail",
        "grade": calculate_grade(percentage) if passed else "F",
    }


def validate_students(students, subjects): 
    if not isinstance(students, list):
        raise ValueError("Students must be provided as a list.")
    if not subjects:
        raise ValueError("At least one subject must be provided.")

    for student in students:
        validate_student(student, len(subjects))


def find_topper(students): 
    if not students:
        return None
    return max(students, key = lambda student: calculate_percentage(student["marks"]))


def calculate_class_average(students): 
    if not students:
        return 0.0
    percentages = [calculate_percentage(s["marks"]) for s in students]
    return sum(percentages) / len(percentages)


def calculate_pass_percentage(students): 
    if not students:
        return 0.0
    passed_count = sum(check_result(s["marks"]) for s in students)
    return passed_count / len(students) * 100


def calculate_subject_averages(students, subjects): 
    if not students:
        return {subject: 0.0 for subject in subjects}

    averages = {}
    for index, subject in enumerate(subjects):
        total = sum(student["marks"][index] for student in students)
        averages[subject] = total / len(students)
    return averages


def display_report(students, subjects): 
    validate_students(students, subjects)

    print("\nSTUDENT PERFORMANCE REPORT")
    print(f"{'Name':<12}{'Total':>8}{'Percentage':>15}{'Result':>12}{'Grade':>10}") 

    for student in students:
        report = analyze_student(student)
        print(
            f"{report['name']:<12}"
            f"{report['total']:>8}"
            f"{report['percentage']:>14.2f}%"
            f"{report['result']:>12}"
            f"{report['grade']:>10}"
        )

    print("\nCLASS SUMMARY")

    topper = find_topper(students)
    if topper is None:
        print("No student data available.")
    else:
        topper_percentage = calculate_percentage(topper["marks"])
        print(f"Topper             : {topper['name']} ({topper_percentage:.2f}%)")

    print(f"Class Average      : {calculate_class_average(students):.2f}%")
    print(f"Pass Percentage    : {calculate_pass_percentage(students):.2f}%")

    print("\nSUBJECT AVERAGES")
    for subject, average in calculate_subject_averages(students, subjects).items():
        print(f"{subject:<18}: {average:.2f}")


def main():
    display_report(students, SUBJECTS)


main()
