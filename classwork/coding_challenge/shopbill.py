def calculate_discount(price, discount):
    final_amount = price - price * (discount / 100)
    return final_amount

price = int(input("Enter the price => "))
discount = int(input("Enter the discount => "))

result = calculate_discount(price, discount)

print("Final amount after discount =>", result)