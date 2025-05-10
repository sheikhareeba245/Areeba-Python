#map() function applies a given function to each item is iterable 
# map(function, iterable)
numbers=[1,2,3,4,5,6,7,8,9]
squared=list(map(lambda x:x**2, numbers))
print(squared)


