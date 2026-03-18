def simple_interest(p, r, t):
    print("Simple Interest is =>", (p * r * t) / 100)

p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

simple_interest(p, r, t)