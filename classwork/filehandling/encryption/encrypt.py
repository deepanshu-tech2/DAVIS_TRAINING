shift = int(input("Enter shift value: "))

with open("input.txt", "r") as f:
    data = f.read()

encrypted = ""

for ch in data:
    if ch.isalpha():  # only encrypt letters
        if ch.islower():
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
    else:
        encrypted += ch   # keep spaces, numbers, symbols same

# write encrypted data
with open("encrypted.txt", "w") as f:
    f.write(encrypted)

print("File encrypted successfully!")
