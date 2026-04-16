with open("data.txt", "r") as f:
    longest_line = ""
    
    for line in f:
        if len(line) > len(longest_line):
            longest_line = line

print("Longest Line:")
print(longest_line.strip())

print("Length:", len(longest_line))
