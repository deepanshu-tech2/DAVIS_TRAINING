def simpleinterest(p,r,t):
    print("your simple interest are =>",(p*r*t)/100)


def si(p,r,t):
    simpleinterest(p,r,t)





p = int(input("enter the principle amount => "))
r = int(input("enter the rate percentage in year=>   "))
t = int(input("enter the time in year=>  "))

si(p,r,t)