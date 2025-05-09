# Nested Loop (Loop Inside a Loop)
# 🔹 Task: Print all combinations from two lists.
colors=["red","orange","peach","black"]
objects=["table","chair","ball","bat"]
for color in colors:
    for obj in objects:
        print(f"{color} {obj}")
        