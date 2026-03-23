def classify(num):
    # Positive / Negative / Zero
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")

    # Even / Odd (nested if)
    if num != 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

# List of numbers
numbers = [5, -3, 0, 8, -2]

for n in numbers:
    classify(n)
    print()
