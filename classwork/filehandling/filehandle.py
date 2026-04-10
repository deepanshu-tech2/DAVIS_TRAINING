# with open("fs.txt", "r") as fs:
#     data = fs.read()
#     print(data)

#  creating a file 
# file = open("file.txt","x")
# file.close()

# with open("file.txt","w+") as file:
#     file.write("hello my name is deepanshu i am from modinagar ")
    
#     file.seek(0)   # 🔥 move pointer to beginning
    
#     datafile = file.read()
#     print(datafile)
user = input("enter a senternce which you want to print in file.txt file=>")    

with open("file.txt","a") as file:
    file.write(user)
    file.seek(0)

with open("file.txt","r") as file:
    print(file.read())
