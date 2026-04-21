data = {"A": [], "B": []}

students = [("Ram", "A"), ("Shyam", "B")]

for name, g in students:
    data[g].append(name)

print(data)
