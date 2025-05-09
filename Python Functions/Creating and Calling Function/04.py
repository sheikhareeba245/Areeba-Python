#Function to print a table of any number
def print_table():
    num=int(input("Enter the number you want to print a table: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
print_table()
