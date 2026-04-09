a = list(map(int, input("Enter numbers separated by space: ").split()))

count = 0
for i in range(len(a)):
    if a[i] > 50:
        count = count + 1

print("Count of numbers greater than 50:", count)
