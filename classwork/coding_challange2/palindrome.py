num = input("Enter a number: ")

reverse = num[::-1]
if(num==reverse):
    print("the number is palindrome=>", reverse)
else:
    print("this number is not palindrome =>",num)
        