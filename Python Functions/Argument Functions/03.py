#Smart grade calculator
def calculate_students_grade(name,marks):
    if marks>=90:
        grade="A"
    elif marks>=80:
        grade="B"
    elif marks>=70:
        grade="C"
    elif marks>=60:
        grade="D"
    else:
        grade="Fail"
    print(f"{name} got Grade {grade}")
calculate_students_grade("Areeba",85)
