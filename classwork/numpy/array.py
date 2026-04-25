import numpy as np 

# creating the array 
# list1= [1,2,4,5,4,5,5,4,5,5,5]
# arr = np.array(list1)
# print(arr)
# print(type(arr))

#  2 dimensional array 
# list2 = [1,2,4,5,6,32,1,5,2,5,4,5,4,5,4]
# list3 = [1,2,4,5,4,5,54,4,5,4,5,4,5,4,4]
# arr1 = np.array([list2,list3])
# print(arr1)

# print(arr1.ndim) 




# ................... numpy array attributes 
# arr1 = np.array([[1,2,4],[4,5,6]])
# print(arr1)
# # ...size 
# print("size",arr1.size)
# # ....shape
# print("shape",arr1.shape)

# zeros array 
# zero_arr = np.ones((2,3))
# print(zero_arr)

# *********full array 
# full_arr = np.full((3,2),7)
# print(full_arr)

# ...........*********iddentity  mattrix 
# id_arr= np.eye(3)
# print(id_arr)

# *****evenly space array 
# print(np.arange(1,5,1))


# **************sspecifice value between a range  equally space 

# print(np.linspace(1,10,4))


# random values array 
# r_arr = np.random.rand(3,2)
# print(r_arr)

# random array in integar 
# r_arr = np.random.randint(1,10,(3,3))
# print(r_arr)

#  array indexing and slicing 
# a = np.array([1,2,4,5,4,5,45,4,5,5])
# print(a)
# print(a[0:5])


# ***** array reshaping  and flatening  ********

# arr1 = np.array([1,2,4,5,6,5])
# print(arr1)
# reshaped = arr1.reshape((6,1))
# print(reshaped)
# reshaped2 = arr1.reshape((2,3))
# print(reshaped2)


# flatening = print("flatenning ",reshaped2.flatten())


# ******array stacking  and splitting  ****
# a =  np.array([2,1,4,5,4,5])
# b =  np.array([2,4,2,4,2,4]) 
# print("vertical stacking =>",np.vstack((a,b)))    # vertical
# print("horizontal stacking=>>>",np.hstack((a,b)))


# c = np.array([[1,2,3],[1,2,3]])
# print(c)
# print("horizontal split=>",np.hsplit(c,3))
# print("vertical split=>>",np.vsplit(c,2))


 


# *****mathematical operation on array ********

# a = np.array([1,2,4,5])
# print("array is =>",a)

# print("addition in array =>", a+10)
# print("substraction operation =>>", a-10)
# print("multiplication opertion =>", a*10)
# print("division operation =>>",a/10)

# print("square of array =>>",np.square(a))
# print("squareroot of array =>>",np.sqrt(a))

# print("sine of array =>>",np.sin(a))  



# ****mathematical operation on multiple array ****


# a =  np.array([2,1,4,5,4,5])
# b =  np.array([2,4,2,4,2,4]) 

# print("addition of both array =>>",np.add(a,b))

# print("multiplication of both array=>",np.multiply(a,b))

# print("dot product =>",np.dot(a,b))
# t = np.array([[1,2,3,4,5],[1,2,3,4,5]])
# print("transpose of t array =>", t.T)   




# ******statical function *******
# a =  np.array([2,1,4,5,4,5])
# print("the sum of array a =>",np.sum(a))
# print("mean of array a =>>", np.mean(a))
# print("median of array a=>>",np.median(a))
# print("max elememt in array =>", np.max(a))
# print("min value in array=>>",np.min(a))


#  ******* array comparson ********* 

# a =  np.array([2,1,4,5,4,5])
# b =  np.array([2,4,2,4,2,4]) 
# print("array a", a)
# print("array b =>",b)
# print(a==b)
# print("comparsion of array a and b =>", np.array_equal(a,b))

# ****broadcasting in array ******
# a =  np.array([2,1,4,5,4,5])
# b =  np.array([2])  
# print("add with beoadcasting in array =>>", a+b)



# *******handling with null vallue 
# data1 = np.array([1,2,3, np.nan,4,np.inf])
# print(data1)
# print("check null value contain in array or not >>",np.isnan(data1))

# print(np.nan_to_num(data1))


# ***save and load array ****** 
# arr = np.array([1,2,4,5,6])
# print("array is =>",arr)
# np.save("my_array.npy",arr)

# loaded_arr = np.load("my_array.npy")
# print("loaded array =>",loaded_arr)



