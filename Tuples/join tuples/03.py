# Problem: Merge Two Tuples and Remove duplicate
# Question: Write a Python program that merges two tuples and removes duplicate values to return a unique tuple.
tuple1=(1,2,3,4,5,10)
tuple2=(6,7,8,9,10,2)
merged_tuple=tuple1+tuple2
print(merged_tuple)
unique_tuple=tuple(set(merged_tuple))
print(unique_tuple)