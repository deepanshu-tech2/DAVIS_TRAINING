def move_zero_in_start(arr):
    j = len(arr) - 1
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]!=0):
            arr[j],arr[i]=arr[i],arr[j]
            j-=1
    return arr

arr= [1,2,0,1,2,4,0,0,0,0,0,1,1,1,1,0,0,0]
print("move zero in starting ",move_zero_in_start(arr))

        
