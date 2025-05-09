#3. Student Result Analyzer (Pass/Fail Counter)
#Input scores of 10 students using a for loop.
#Count how many students scored >= 40 (pass)
#Use pass in loop body before logic as a placeholder
#Print total passes and fails
pass_count=0
fail_count=0
for i in range(10):
    pass
score=int(input(f"Enter score for students {i+1}: "))
if score>=40:
    pass_count+=1
else:
    fail_count+=1
print(f"Passed Students:{pass_count},Failed Students: {fail_count} ")
