# Problem:
# Input: A string command for food order.
# "pizza" or "burger" or "fries" → print "Fast Food Selected"
# "tea" or "coffee" or "juice" → print "Beverage Selected"
# Anything else → print "Item not on menu"
# Use match-case with | to combine options.
order=input("Kindly Sir! Place your order: ")
match order:
    case "pizza"|"burger"|"Fries":
        print("Fast Food Selected: ")
    case "tea"|"coffee"|"juie":
        print("Beberage Selected: ")
    case _:
        print("Item not on menu: ")
        