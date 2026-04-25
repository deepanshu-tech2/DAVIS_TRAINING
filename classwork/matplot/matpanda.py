import pandas as pd 
#  data 

data = {
    "month" : ["jan","feb","mar","apr"],
    "sales":[12000,12000,12000,12000,]

}
df= pd.DataFrame(data)
import matplotlib.pyplot as plt 
# plt.bar(df["month"],df["sales"])
# plt.title("matplotlib with pandas ")
# plt.xlabel("month ")
# plt.ylabel("sales")
# plt.show()


# ********** save plots or charts 
plt.bar(df["month"],df["sales"])
plt.title("matplotlib with pandas ")
plt.xlabel("month ")
plt.ylabel("sales")
plt.savefig(r"C:\Users\deepa\Desktop\davistraining\classwork\matplot\monthly_sales.png")
plt.show()