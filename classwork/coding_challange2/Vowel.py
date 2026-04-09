# write a program to check the anter char is vowel or not 
a = input("enter a charachter =>")
if(len(a)>1):
    print("please enter a single character")

else:
    if ( a=='a'or a== 'e' or a == 'i' or a=='o' or a=='u'):
        print("this character is vowel",a)
    else:
     print("this character is not vowel=>",a)        

