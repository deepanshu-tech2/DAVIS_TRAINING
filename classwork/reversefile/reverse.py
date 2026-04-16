# read file
with open("input.txt", "r") as f:
    lines = f.readlines()

# reverse lines
lines.reverse()

# write to new file
with open("output.txt", "w") as f:
    f.writelines(lines)

print("File reversed successfully!")
