def table(n):
    if n < 0:
        print("Negative number not allowed")
        return

    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter number: "))
table(num)
