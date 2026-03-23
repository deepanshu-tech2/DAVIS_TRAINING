t = (1,4,2,4,5,3,1,4,8,9,1,2)
min_val= max_val=t[0]
for i in t:
    if i >max_val:
        max_val = i 
    if i < min_val :
        min_val = i 


print("maxvalue is =>",max_val ,"min value is ",min_val)            