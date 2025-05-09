#Food Bill Calculator
def calculate_bill(item,quantity):
    price_per_item=100
    total_price=price_per_item*quantity
    print(f"Your order {quantity},{item}")
    print(f"Total bill is: Rs.{total_price}")
calculate_bill("Burger",5)
