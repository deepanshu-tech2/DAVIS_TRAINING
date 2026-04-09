str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Normalize (lowercase and remove spaces)
s1 = str1.replace(" ", "").lower()
s2 = str2.replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")
