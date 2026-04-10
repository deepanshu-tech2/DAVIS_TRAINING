# write a program to count the no of vowels into the given file 
vowels = "aeiouAEIOU"
count = 0
with open("nextline.txt","r") as file :
    data = file.read()

for ch in data:
    if ch in vowels:
        count += 1

print("Number of vowels in file:", count)

