lst = [1, 2, 3, 2, 4, 1, 5]

result = []

for i in lst:
    if lst.count(i) == 1:
        result.append(i)

print("Original list:", lst)
print("After removing all duplicates:", result)