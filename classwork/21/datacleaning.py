clean = []

with open("dirty.txt") as f:
    for line in f:
        if line.strip():
            clean.append(line.strip())

print(clean)
