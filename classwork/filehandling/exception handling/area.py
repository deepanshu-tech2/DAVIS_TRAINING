import math

try:
    r = float(input("Enter radius of circle: "))

    if r < 0:
        raise ValueError("Radius cannot be negative")

    area = math.pi * r * r
    perimeter = 2 * math.pi * r

    print("Area of circle:", round(area, 2))
    print("Perimeter (Circumference):", round(perimeter, 2))

except ValueError as e:
    print("Invalid input:", e)

except Exception as e:
    print("Error:", e)
