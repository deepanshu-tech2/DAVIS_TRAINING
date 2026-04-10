#  every sentence must be in new line 
# sentence = input("enter the 20 sentence and must be seprated by comma all => ")
# lines = sentence.split(" ")
# lines = [line.strip() +"\n"for line in lines]
# with open("nextline.txt","w") as file:
#     file.writelines(lines)
#     print("file content add succesfully")
#     file.seek(0)

# with open("nextline.txt","r") as file:
#     print("file content => \n")
#     print(file.readlines())    

# file.close()    

word = []
for i in range(20):
    data= input()
    word.append(data +"\n")

with open("nextline.txt","w") as file:
    file.writelines(word)
    print("file content add succesfully")
    file.seek(0)
file.close()

with open ("nextline.txt","r") as file:
    print("file content is =>")
    print(file.read())

file.close()    
