#filter() function is used to filter out elements from the iterable based on condition
#filter(function, iterable)
numbers=[1,2,3,45,6,7,8,9,10]
even_number=list(filter(lambda x: x%2==0,numbers))
print(even_number)