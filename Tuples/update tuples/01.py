#Once tuple is created ypu cannot change the values of it because tuple item are unchangeable but there is workaround you can change,add or remove item but first you convert your tuple into list then make changes and after changes you convert your list back intoi tuple
x=("banana","apple","cherry")
#converting tuple into list
y=list(x)
y[1]="kiwi"
x=tuple(y)
print("Changes are made: ",x)
