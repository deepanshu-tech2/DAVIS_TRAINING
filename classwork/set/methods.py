# create set two set 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a =", a)
print("b =", b)
print("------------------------------------")

# add()  
a.add(10)
print("add(10):", a)
print("------------------------------------")

# update()
a.update([20, 30])
print("update([20,30]):", a)
print("------------------------------------")

# copy()
c = a.copy()
print("copy():", c)
print("------------------------------------")

# remove()
a.remove(30)
print("remove(30):", a)
print("------------------------------------")

# discard()
a.discard(100)   # no error
print("discard(100):", a)
print("------------------------------------")

# pop()
x = a.pop()
print("pop(): removed", x)
print("after pop:", a)
print("------------------------------------")

# union()
print("union():", a.union(b))
print("------------------------------------")

# intersection()
print("intersection():", a.intersection(b))
print("------------------------------------")

# difference()
print("difference(a-b):", a.difference(b))
print("------------------------------------")

# symmetric_difference()
print("symmetric_difference():", a.symmetric_difference(b))
print("------------------------------------")

# intersection_update()
d = {1, 2, 3, 4}
d.intersection_update({3, 4, 5})
print("intersection_update():", d)
print("------------------------------------")

# difference_update()
e = {1, 2, 3, 4}
e.difference_update({3, 4})
print("difference_update():", e)
print("------------------------------------")

# symmetric_difference_update()
f = {1, 2, 3}
f.symmetric_difference_update({3, 4, 5})
print("symmetric_difference_update():", f)
print("------------------------------------")

# isdisjoint()
print("isdisjoint():", {1, 2}.isdisjoint({3, 4}))
print("------------------------------------")

# issubset()
print("issubset():", {1, 2}.issubset({1, 2, 3, 4}))
print("------------------------------------")

# issuperset()
print("issuperset():", {1, 2, 3, 4}.issuperset({1, 2}))
print("------------------------------------")

# clear()
g = {7, 8, 9}
g.clear()
print("clear():", g)
print("------------------------------------")