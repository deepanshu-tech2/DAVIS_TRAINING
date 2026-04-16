with open("remove.txt", "r") as f:
    lines = f.readlines()

unique_lines = []
seen = set()

for line in lines:
    if line not in seen:
        unique_lines.append(line)
        seen.add(line)

with open("remove.txt", "w") as f:
    f.writelines(unique_lines)

print("Duplicate lines removed (order preserved)!")
