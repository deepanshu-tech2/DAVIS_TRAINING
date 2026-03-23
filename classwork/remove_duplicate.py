lst = [1, 2, 3, 2, 4, 2, 5]

x = int(input("Enter number to remove duplicates of: "))

seen = False
result = []

for i in lst:
    if i == x:
        if not seen:
            result.append(i)
            seen = True
    else:
        result.append(i)

print("Original list:", lst)
print("After removing duplicate of", x, ":", result)