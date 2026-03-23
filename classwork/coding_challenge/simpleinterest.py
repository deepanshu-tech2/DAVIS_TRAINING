def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


# Taking input
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate (%): "))
time = int(input("Enter the time (years): "))

# Function call
result = calculate_simple_interest(principal, rate, time)

print("Total interest is =>", result)