#intersection () will return a new set that contains only values that are present in both sets
set1 = {"apple", "banana", "cherry","google"}
set2 = {"google", "microsoft", "apple"}
set3=set1.intersection(set2)
print("Duplicate values are exluded: ",set3)
#the & operator do this same 
set1 = {"apple", "banana", "cherry","google"}
set2 = {"google", "microsoft", "apple"}
set3=set1&set2
print("Duplicate values are exluded: ",set3)
