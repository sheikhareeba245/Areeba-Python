# Problem:
# Take a number input.
# If the number is positive:
# check if it is even or odd using nested if
# If negative: print "Negative number"
# If zero: print "Zero"
number=int(input("Enter your number: "))
if number>0:
    print("Number is positive: ")
    if number %2==0:
        print("Number is even:")
    else:
        print("Number is odd: ")
elif number<0:
    print("Number is negative: ")
else:
    print("Number is zero: ")
