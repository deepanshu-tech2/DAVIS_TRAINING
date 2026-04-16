# open both files and read lines
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# merge both
merged_lines = lines1 + lines2

# write with line numbers
with open("merged.txt", "w") as f:
    for i, line in enumerate(merged_lines, start=1):
        f.write(f"{i}. {line}")

print("Files merged successfully with line numbers!")
