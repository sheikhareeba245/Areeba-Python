#ok now we use *args and **kwargs both in one problem
#Create a student profile generator that
#Uses *args to list hobbies or skills
#Uses **kwargs for subject marks
def student_profile(name,*skills,**marks):
    print(f"Student Name:{name}")
    print("Skills/Hobbies")
    for skill in skills:
        print(f"Student Skills: {skill}")
    print("\n Student Marks: ")
    total=0
    for subject, score in marks.items():
        print(f"{subject}: {score}")
        total +=score
    print(f"Total Marks: {total}")
    print(f"Average Marks: {total/len(marks):.2f}")
student_profile("Areeba","Python",Math=90,Urdu=75,Computer=80)
