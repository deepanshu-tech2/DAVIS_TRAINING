def move_zero(arr):
    j = 0
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[j],arr[i]= arr[i], arr[j]
            j+=1
    return arr
arr = [1,5,0,1,4,5,0,1,0,0,4,0]
print("mpve zero in last " , move_zero(arr))