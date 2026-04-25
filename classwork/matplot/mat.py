import matplotlib.pyplot as plt 

# x = [2,1,4,5,4,5,2,1]
# y = [2,4,5,1,2,1,4,2]

#  create the first chart 
# x = [2,1,4,5,4,5,2,1]
# y = [2,4,5,1,2,1,4,2]
# plt.plot(x,y)
# plt.show()



# plt.figure(figsize=(6,4))

# customized chart 
# plt.plot(x, y, color="red", marker="o", linestyle="dashed", linewidth=2, markersize=12)
# plt.show()





#  add the haeding in the matplot library graph 
# plt.figure(figsize=(4,5))

# plt.plot(x, y, color="red", marker="o", linestyle="dashed", linewidth=2, markersize=12)
# plt.title("your name ")
# plt.xlabel("x axis ka label hai ")
# plt.ylabel("y axis ka label hai ")
# plt.show()


# .........multiple lines and lagents 

# x = [1,2,3,4,5,6,7,8,9,10]
# y1 =[10,20,30,40,50,10,40,50,60,80]
# y2 = [20,30,40,50,60,40,41,50,50,90]
# plt.plot(x,y1,label="sales 2024")
# plt.plot(x,y2,label= "2025 data ")
# plt.title("yoy sales ")
# plt.xlabel("month ")
# plt.ylabel("sasles ")
# plt.legend()
# plt.show()


# bar chart 
# x = [1,2,3,4,5,6,7,8,9,10]
# y =[10,20,30,40,50,10,40,50,60,80]
# plt.bar(x,y)
# plt.title("bar chart example")
# plt.show()


#  histogram 
# import random
# data = [random.randint(1,10) for _ in range(100)]
# plt.hist(data , bins=20)
# plt.title("histogram title")
# plt.show()


#  pie chart 
# ===>>>>>   used to show part to whole relatioship/data 

# category  = [1,2,3,4,5,6,7,8,9,10]
# sales  =[10,20,30,40,50,10,40,50,60,80]
# plt.pie(sales,labels=category,autopct='%1.1f%%' startangle=50)
# plt.show()


#    scatter plot 
# ==>> used to find relatioship between variables 
# y1 = [10,20,30,40,50,60]
# y2 = [20,30,40,50,60,70]
# plt.scatter(y1,y2)
# plt.title("scatter plot example ")
# plt.show()

# **************** subplots 
# ===>>>> show multiple chart in simgle chart 
# data 1 - bar chart 
categories = ["mon","tue","wed","thu","fri"]
sales = [10,20,30,40,50]


#  data 0 - scatter plot 
y1 = [10,20,30,40,50,60]
y2 = [20,30,40,50,60,70]

plt.figure(figsize=(10,6))

#  first plot bar char 
# plt.subplot(1,2,1)   # firt - row  , column , position 
# plt.scatter(categories,sales)
# plt.title("weekly sales ")
# plt.xlabel("week days ")
# plt.ylabel("sales") 


# plt.subplot(1,2,2)   # firt - row  , column , position 
# plt.bar(y1,y2)
# plt.title("user example  ")
# plt.xlabel("user 1  ")
# plt.ylabel("user 2 ")
# plt.show() 
