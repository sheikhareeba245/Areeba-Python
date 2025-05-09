#2. Online Shopping Discount Validator
#A customer can add 5 products.
#If any product costs more than ₹10,000 → apply "Premium Item"
#If total exceeds ₹50,000 → stop further entries with break
#Use for, if, break, and continue for skipping items
total=0
for i in range(5):
    price=float(input(f"Enter the price for product {i+1}: "))
    if price>10000:
        print("Premium Item")
    total+=price
    if total>50000:
        print("Budget Limit reached Stop further entries")
        break
print("Total Spend: ",total)