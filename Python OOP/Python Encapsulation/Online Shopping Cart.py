# Online Shopping Cart
# Task:
# Create a class ShoppingCart with:
# A private attribute __items (a list)
# add_item(item) method to add items to the cart
# remove_item(item) method to remove items
# view_cart() to display current items
class ShoppingCart:
    def __init__(self):
        self.__list=[]
    def add_item(self,item):
        if item.strip():
            self.__list.append(item)
            print(f"Items added Successfully: {item}")
        else:
            print("Item name cannot be empty")
    def remove_item(self,item):
        if item in self.__list:
            print(f"Item removed succesfully: {item}")
        else:
            print("Items not found in the cart")
    def view_cart(self):
        if self.__list:
            print(f"Items in the cart: {self.__list}")
        else:
            print("Cart is empty")
cart=ShoppingCart()
# cart.add_item("Laptop")
# cart.add_item("Phone")
# cart.add_item("Shoes")
# cart.add_item("Milk")
# cart.view_cart()
# cart.remove_item("Milk")
while True:
    print("\n Choose your Option \n1 Add Item \n2 Remove Item \n3 View Cart \n4 Exit")
    choice=input("Enter your Choice between 1-4: ")
    if choice =="1":
        item=input("Enter the item you want to add: ")
        cart.add_item(item)
    elif choice =="2":
        item=input("Enter the item yoou want to remove: ")
        cart.remove_item(item)
    elif choice =="3":
        cart.view_cart()
    else:
        print("Thankyou for shopping Have a Nice Day")
