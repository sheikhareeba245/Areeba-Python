#iterator is an object in python which return items one by one from any list,tuple
#iterator use two concepts iter(),next()
#iter() use to convert any iterable like list into iterator
#next()take next item from the list
fruits=["apple","banana","grapes","mango"]
it=iter(fruits)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

