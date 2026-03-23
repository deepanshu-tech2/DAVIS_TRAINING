
arr = [5, 2, 9, 1, 7, 3, 8, 6, 4, 0]

# Bubble Sort (Descending)
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] < arr[j + 1]:   # Change sign for descending
            # Swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted list (Descending):", arr)
