#Practicing array with array module
#Firstly always inport module
import array
# Problem 1:
# Create an array of integers with the values [5, 10, 15, 20, 25] and print all its elements using a loop.
arr=array.array('i',[5,10,15,20,25])
for num in arr:
    print(num)
# Problem 2: 
# Add 30 to the end of the array. Then insert 12 at index 1.
arr.append(30)
arr.insert(1,12)
print(arr)
# Problem 3:
# Reverse the entire array and print it.
arr.remove(12)
arr.pop(5)
print(arr)
#Problem 4:
#Print the value at index 3.
print(arr[3])
# Problem 5:
# Reverse the entire array and print it.
arr.reverse()
print("Reversed array: ",arr)
# Problem:
# Find the index of the value 25.
index=arr.index(25)
print("Index array: ",index)
# Problem:
# Find the total sum of all the values in the array.
total=sum(arr)
print("Sum: ",total)
# Problem:
# Create an array of float numbers [1.2, 3.4, 5.6] using the correct type code.
float_arr=array.array('f',[1.2,3.4,5.6])
print("Floated Array: ",float_arr)
