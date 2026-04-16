while True:
    print("1 : Enter the string")
    print("0 : Exit")

    n = int(input("Enter choice (1/0): "))

    if n == 0:
        break

    if n == 1:
        a = input("Enter the string: ")

        freq = {}   # dictionary

        for ch in a:
            if ch != " ":   # ignore spaces (optional)
                freq[ch] = freq.get(ch, 0) + 1

        # store in file
        with open("article.txt", "a") as f:
            f.write(str(freq) + "\n")

        print("Character frequency stored successfully!\n")
