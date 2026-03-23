def interest(p,r,t):
    print("simple interest are => " , (p*r*t)/100)


def simpleinterest(p,r,t):
    interest(p,r,t)


p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

simpleinterest(p,r,t)