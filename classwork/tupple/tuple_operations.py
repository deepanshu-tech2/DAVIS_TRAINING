# Tuple all operations in one code

t = (10, 20, 30, 20, 40, 50)

print("Original tuple:", t)
print("------------------------------------")

# 1. Indexing
print("First element:", t[0])
print("Last element:", t[-1])
print("------------------------------------")

# 2. Slicing
print("Slicing [1:4]:", t[1:4])
print("------------------------------------")

# 3. Length
print("Length of tuple:", len(t))
print("------------------------------------")

# 4. Count
print("Count of 20:", t.count(20))
print("------------------------------------")

# 5. Index
print("Index of 30:", t.index(30))
print("------------------------------------")

# 6. Membership
print("20 in tuple:", 20 in t)
print("100 in tuple:", 100 in t)
print("------------------------------------")

# 7. Looping
print("Tuple elements:")
for i in t:
    print(i, end=" ")
print()
print("------------------------------------")
# 8. Concatenation
t2 = (60, 70)
new_tuple = t + t2
print("After concatenation:", new_tuple)
print("------------------------------------")

# 9. Repetition
print("Tuple repetition:", t2 * 2)
print("------------------------------------")

# 10. Nested tuple
nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("Access nested element:", nested[1][0])
print("------------------------------------")

# 11. Convert tuple to list
lst = list(t)
print("Tuple to list:", lst)
print("------------------------------------")

# 12. Modify using list
lst.append(99)
t = tuple(lst)
print("After adding element using list conversion:", t)
print("------------------------------------")

# 13. Deleting tuple
a = (1, 2, 3)
print("Before delete:", a)
del a
print("------------------------------------")
# print(a)   # this will give error because tuple is deleted

# 14. Min, Max, Sum
num = (5, 2, 8, 1, 9)
print("Min:", min(num))
print("Max:", max(num))
print("Sum:", sum(num))
print("------------------------------------")

# 15. Iteration with index
print("Using index:")
for i in range(len(t)):
    print("Index", i, "=", t[i])

print("------------------------------------")    