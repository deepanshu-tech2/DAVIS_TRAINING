#  every sentence must be in new line 
sentence = input("enter the 20 sentence and must be seprated by comma all => ")
lines = sentence.split(" ")
lines = [line.strip() +"\n"for line in lines]
with open("nextline.txt","w") as file:
    file.writelines(lines)
    print("file content add succesfully")
    file.seek(0)

with open("nextline.txt","r") as file:
    print("file content => \n")
    print(file.read())    

file.close()    