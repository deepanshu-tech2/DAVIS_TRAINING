def even(n):
    print("the list of even number are =>")
    for i in range(1,n+1,1):
        if(i%2==0):
            print(i)

def alleven(n):
    even(n)

def evennumber(n):
    alleven(n)



n = int(input("enter the range=>  "))
evennumber(n)