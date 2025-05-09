#the intersection_update()method will also keep the duplicate values but they change in original set not return a new set
set1={"bat","ball","table","chair","spoon","fork"}
set2={"ball","door","chair","spoon","fork"}
set1.intersection_update(set2)
print("Duplicated values: ",set1)
#The values True and 1 are considered the same value. The same goes for False and 0.
set1={"apple",True,1,"grapes",False,0,2}
set2={"banana",True,1,"pineapple",0,False,90}
set1.intersection_update(set2)
print("Intersection update: ",set1)
