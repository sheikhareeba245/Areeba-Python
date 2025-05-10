#Given a list like this: [(2, 5), (1, 2), (4, 4), (2, 3)]
#Use lambda to sort by the second element of each tuple.
list_of_Numbers=[(2,5),(1,2),(4,4),(2,3)]
sorted_list=sorted(list_of_Numbers, key=lambda x:x[1])
print(sorted_list)
