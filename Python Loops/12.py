#the else block will not be executed if the loop is topped by the break statement
fruits=["apple","mango","cherry","orange","pineapple","grapes","peach"]
for x in range(6):
    if x==3:
        break
    print(x)
else:
    print("Loop is executed completely")
    