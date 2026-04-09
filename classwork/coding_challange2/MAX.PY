# Take input from user
a = list(map(int, input("Enter numbers separated by space: ").split()))

# Assume first element is maximum
max_val = a[0]

# Compare with remaining elements
for i in range(1, len(a)):
    if a[i] > max_val:
        max_val = a[i]

print("Maximum value:", max_val)
