text = input("Enter a sentence: ")

words = text.split()
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
