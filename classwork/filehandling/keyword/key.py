keyword = input("Enter keyword to search: ")

with open("data.txt", "r") as f:
    found = False
    for line in f:
        if keyword.lower() in line.lower():   # case-insensitive search
            print(line.strip())
            found = True

if not found:
    print("No matching lines found.")
