# Shopping Cart System 
# Question:Write a Python program to create a shopping cart system where users can:
# Add items to the cart
# Remove items from the cart
# View the cart
# Checkout and display the final cart
cart=[]
while True:
    print("\n1. Add Item\n2. Remove Item\n3. View Cart\n4. Checkout")
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=input("Enter the item you add: ")
        cart.append(item)
        print(f"{item} added to cart!")
    elif choice==2:
        item=input("Enter the item you want to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed successfully")
        else:
            print("Item not found! ")
    elif choice==3:
        print("Your shopping cart:",cart)
    elif choice==4:
        print("Your final shopping cart......!",cart)
    break
else:
    print("Invalid Choice!")


        
    

