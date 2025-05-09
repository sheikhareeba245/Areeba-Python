#shopping cart
def shopping_cart(*items):
    print("Your shopping cart: ")
    print(f"Total items: {items}")
    print("Items")
    for item in items:
        print(f"- {item}")
shopping_cart("milk","eggs","bread","juice","lays")
