# import summodule
# num1 = int(input("enter the first number=>"))
# num2 = int(input("enter the first number=>"))
# result = summodule.find_sum(num1,num2)
# print("sum is=>",result)



#  using from modulename import * 
from summodule import * 

num1 = int(input("enter the first number=>"))
num2 = int(input("enter the first number=>"))
result = find_sum(num1,num2)
print("sum is=>",result)