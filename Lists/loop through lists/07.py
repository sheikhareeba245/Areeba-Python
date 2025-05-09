# Loop Through Two Lists at Once Using zip()
# 🔹 Task: Print corresponding elements from two lists.
names=["areeba","sidrah","akram","jawad"]
ages=["23","24","25","26","27"]
for name,age in zip(names,ages):
    print(f"{name} is {age} years old")

