def eligiblevote(age):
    if(age>=18):
        print("you are eligible for vote => " ,age)

    else:
        print("you are not eligible for vote",age)    


age = int(input("enter your age => "))
eligiblevote(age)
