# /largest number among three 
a = int(input("enter the first number =>"))
b = int(input("enter the second number =>"))
c = int(input("enter the third  number =>"))

if(a>b):
    if(a>c):
        print("a is largest number=>",a)
    else:
        print("c is largest number=>",c)
else:
    if(b>c):
          print("b is largest number",b)
    else:
        print("c is largest number => ",c)                