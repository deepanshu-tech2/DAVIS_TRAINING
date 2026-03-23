def even(n):
    for i in range(1,n+1,1):
        if(i%2==0):
            print(i)

n = int(input("enter the range of even number => "))
even(n)            