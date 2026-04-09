text = input("Enter a string: ")

result = ""
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print("Modified string:", result)
