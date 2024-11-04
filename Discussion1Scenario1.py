# Let's consider this list as transactions of a certain day in  a retail store
transactions = [100, 250, 75, 300, 120]
total_sales = 0

for transaction in transactions:
    total_sales += transaction  # We are adding each value from the list to out total

print("Total sales for the day:", total_sales)
