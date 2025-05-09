# Change Product Price in Catalog (No function)
# You have a product inventory.
# Change the price of "mouse" to 22.0.
inventory={
    "mouse":21.00,
    "keyboard":25.00,
    "CPU":50.00,
}
inventory.update({"mouse":"22.00"})
print(inventory)
