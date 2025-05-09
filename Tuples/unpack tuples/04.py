#what if we only need first and last values in the tuple
numbers=(10,20,30,40,50)
(first,*_,last)=numbers#_dummy variable
print(first)
print(last)