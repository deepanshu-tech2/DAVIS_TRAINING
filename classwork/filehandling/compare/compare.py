with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# convert file2 lines to set for fast lookup
set2 = set(lines2)

# find unique lines in file1
for line in lines1:
    if line not in set2:
        print(line.strip())
