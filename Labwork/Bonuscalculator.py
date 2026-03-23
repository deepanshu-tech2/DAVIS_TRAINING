def calculate_bonus(salary, years):
    if years >= 10:
        bonus = salary * 0.20
    elif years >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    return bonus

# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(n):
    salary = float(input("Enter salary: "))
    years = int(input("Enter years of experience: "))

    bonus = calculate_bonus(salary, years)
    print("Bonus:", bonus)
    print()
