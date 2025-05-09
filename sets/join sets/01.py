#in python we use several methods to join sets for join two set we use method union() and update()
set1={1,2,3,4,5}
set2={6,7,8,9,10}
set3=set1.union(set2)
print("All items in the set are joined: ",set3)
#we also use | oprerator to join two sets and we wil get same result
set1={1,2,3,4,5}
set2={6,7,8,9,10}
set3=set1|set2
print("All items in the set are joined: ",set3)
