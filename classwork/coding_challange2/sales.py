# Take input from user as a list
sales = list(map(int, input("Enter 7 days sales separated by space: ").split()))

# Calculate total sales
total = sum(sales)

print("Total Weekly Sales =", total)
