#symmetric_difference method will keep only the elements that are NOT present in both sides
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#we can use ^ operator to symmetric_difference 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1^set2
print(set3)