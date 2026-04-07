p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

def simple_interest(p, r, t):
    return (p * r * t) / 100

print("Simple Interest =", simple_interest(p, r, t))
