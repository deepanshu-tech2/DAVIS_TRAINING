# Initial dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print("Initial Dictionary:", d)

# 1. get()
print("\nget('a'):", d.get('a'))
print("get('z', 0):", d.get('z', 0))  # default value

# 2. keys()
print("\nKeys:", d.keys())

# 3. values()
print("Values:", d.values())

# 4. items()
print("Items:", d.items())

# 5. update()
d.update({'d': 4, 'e': 5})
print("\nAfter update():", d)

# 6. pop()
d.pop('a')
print("After pop('a'):", d)

# 7. popitem()
d.popitem()
print("After popitem():", d)

# 8. setdefault()
d.setdefault('f', 6)
d.setdefault('b', 100)  # won't change existing
print("\nAfter setdefault():", d)

# 9. copy()
d_copy = d.copy()
print("\nCopy of dictionary:", d_copy)

# 10. clear()
temp = {'x': 10, 'y': 20}
temp.clear()
print("\nAfter clear():", temp)

# 11. fromkeys()
keys = ['p', 'q', 'r']
new_dict = dict.fromkeys(keys, 0)
print("\nFromkeys():", new_dict)

# 12. Check key exists
print("\nIs 'b' in dictionary?", 'b' in d)

# 13. Loop through dictionary
print("\nLooping through dictionary:")
for key, value in d.items():
    print(key, ":", value)

# 14. Insert / Update manually
d['z'] = 100
print("\nAfter inserting 'z':", d)

# Final dictionary
print("\nFinal Dictionary:", d)
