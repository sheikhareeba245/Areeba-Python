#Sort Products by Name Length
products=[("Apple",139),("Orange",200),("Mango",123)]
sorted_products=sorted(products,key=lambda x:len(x[0]))
print(sorted_products)