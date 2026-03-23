list = [1,2,4,3,4,5,7,8,3,4,1,1,2,3,4]
result = []
for i in list:
    if i not in result:
        result.append(i)

print("after removing the duplicate element =>", result)