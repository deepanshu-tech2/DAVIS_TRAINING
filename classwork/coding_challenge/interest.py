def simpleinterst(p,r,t):
    simple_interest = (p*r*t)/100
    print("your simple interest is => " , simple_interest)


p = int(input("enter the principle amount => "))   
r = int(input("enter the rate => "))
t = int(input("enter the time in year => ")) 
simpleinterst(p,r,t)