# ==============================
# STRING IN PYTHON - FULL PROGRAM
# ==============================

# 1. Creating Strings
print("---- Creating Strings ----")
s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line string"""

print(s1)
print(s2)
print(s3)


# 2. Indexing
print("\n---- Indexing ----")
s = "Python"
print("First character:", s[0])
print("Last character:", s[-1])


# 3. Slicing
print("\n---- Slicing ----")
print("0 to 3:", s[0:3])
print("From 2:", s[2:])
print("Up to 4:", s[:4])


# 4. Immutability
print("\n---- Immutability ----")
# s[0] = 'Y' ❌ Not allowed
new_s = "Y" + s[1:]
print("Modified string:", new_s)


# 5. String Methods
print("\n---- String Methods ----")
text = "  hello world  "

print("Lower:", text.lower())
print("Upper:", text.upper())
print("Strip:", text.strip())
print("Replace:", text.replace("hello", "hi"))
print("Split:", text.split())


# 6. Join Method
print("\n---- Join ----")
lst = ['a', 'b', 'c']
print("Joined:", "-".join(lst))


# 7. Find and Count
print("\n---- Find & Count ----")
word = "banana"
print("Find 'a':", word.find("a"))
print("Count 'a':", word.count("a"))


# 8. Startswith & Endswith
print("\n---- Startswith / Endswith ----")
print(word.startswith("ba"))
print(word.endswith("na"))


# 9. Loop through String
print("\n---- Loop ----")
for ch in "ABC":
    print(ch)


# 10. String Operations
print("\n---- Operations ----")
print("Concatenation:", "Hello" + " World")
print("Repetition:", "Hi " * 3)


# 11. Membership Check
print("\n---- Membership ----")
print("py" in "python")


# Final Output
print("\n✅ All string operations executed successfully!")
