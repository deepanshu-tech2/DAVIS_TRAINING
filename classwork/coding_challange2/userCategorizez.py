# an online platfrom chatarized user by age group 
age = int(input("enter user age in years => "))

if(age<18):
    print("this user is minor=>",age)
elif(age>=18 and age<50):
    print("this user is adult => " , age)

else:
    print("this user is senior => ",age)
    
            