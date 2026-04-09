# A payment system processes only numbers divisible by both 3 and 5. 
# Task: 
# Write a program to check if a number satisfies this condition. 
num = int(input("enter any integar number =>"))
if num % 3 == 0 and num % 5 == 0:
    print("Number is valid (divisible by both 3 and 5)")
else:
    print("Number is not valid")