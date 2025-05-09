# Loop Through List with continue (Skip an Item)
# 🔹 Task: Skip a specific value while looping.
numbers=[1,2,3,4,5]
for num in numbers:
    if num==3:
        continue
    print(num)