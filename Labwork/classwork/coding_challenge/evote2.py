def check_vote(age):
    return age >= 18

age = int(input("Enter your age: "))

print("Eligible for vote" if check_vote(age) else "Not eligible")