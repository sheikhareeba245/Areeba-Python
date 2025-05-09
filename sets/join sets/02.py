#we can use union() method to join multiple sets
set1={1,2,3,4,5}
set2={'A','B','C','D','E','F'}
set3={"Areeba","Jawad","Aiman"}
set4={9.9,8.7,6.7,4.5,2.3}
set5=set1.union(set2,set3,set4)
print("All sets are combined: ",set5)
#we use this with| operator
set1={1,2,3,4,5}
set2={'A','B','C','D','E','F'}
set3={"Areeba","Jawad","Aiman"}
set4={9.9,8.7,6.7,4.5,2.3}
set5=set1|set2|set3|set4
print("All sets are combined: ",set5)
