#Python does not have built-in support for array
#so we use lists as array to store elements
#because we store all types of data in lists like
#list=["Areeba",12,4.5]
#Python ma eik array module ha but is ma hum eik hi data type ka data store kar sakta hain
#If you want to work with arrays you install numpay libray for this
#use list as array
my_array=[10,20,30,40,50,60,70,80,90,100]
print(my_array)
#what if I want to access elements
print(my_array[3])#so I want to access element 3 in my array
#so  now I want to update my array like I want that change element in a specific index
my_array[2]=99 # so I want that in index 2 element change to 30 to 99
print(my_array)
#so I want to add element in my array
my_array.append(77) #add element 77 in my array
print(my_array)
#ok now I want to insert an element at a specific index
my_array.insert(1,15) #I insert element 15 at index 1
print(my_array)
#Ok Now I want to remove element in my array
my_array.remove(77) #I remove element 77 from my array
print(f"Removing element{my_array}")
#ok now I want to remove element at a specific index
my_array.pop(7)
print(f"Pop element at a specific index {my_array}")
#Now I want to know the lenght of my array
print("Lenght of my array:",len(my_array))
#Now I am looping through array
for item in my_array:
    print(my_array)