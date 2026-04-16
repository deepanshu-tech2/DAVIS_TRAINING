import re

# read data from file
with open("data.txt", "r") as f:
    data = f.read()

# regex pattern for email
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)

# remove duplicates (optional)
emails = list(set(emails))

# write emails to new file
with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted successfully!")
