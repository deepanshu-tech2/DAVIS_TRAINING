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
a = np.array([1,2,4,5,4,5,45,4,5,5])
print(a)
print(a[0:5])