def is_palindrome(s):
    s = str(s)
    rev = ""

    for i in range(len(s)-1, -1, -1):
        rev += s[i]

    if s == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Example
val = input("Enter value: ")
is_palindrome(val)
