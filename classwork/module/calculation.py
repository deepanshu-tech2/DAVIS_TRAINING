# import numericcalculation
from numericcalculation import *

while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Difference")
    print("3. Product")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        print("Program exited.")
        break

    a = int(input("Enter first number => "))
    b = int(input("Enter second number => "))

    if choice == 1:
        print("Addition =>", calculateAddition(a, b))

    elif choice == 2:
        print("Difference =>", calculateDifference(a, b))

    elif choice == 3:
        print("Product =>", calculateProduct(a, b))

    elif choice == 4:
        if b != 0:
            print("Division =>", calculatedivide(a, b))
        else:
            print("Error: Division by zero!")

    elif choice == 5:
        print("Modulus =>", calculatemodulus(a, b))

    else:
        print("Invalid choice! Please select between 1-6.")
