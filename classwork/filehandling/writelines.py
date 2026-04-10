# Take bulk input from user (one line, separated by comma)
data = input("Enter multiple lines separated by comma: ")

# Convert input into list
lines = data.split(",")

# Add newline to each line
lines = [line.strip() + "\n" for line in lines]

# Write all lines at once
with open("file.txt", "w") as file:
    file.writelines(lines)

print("Data written successfully!")

# Read and display back to user
with open("file.txt", "r") as file:
    print("\nFile Content:")
    print(file.read())
