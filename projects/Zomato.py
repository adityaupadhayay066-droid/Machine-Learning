import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Zomato data .csv")
df.columns = df.columns.str.strip()
print(df.columns)
print(df.head(),"\n")
print(df.tail ())

def Remove(value):
    value = str(value).split("/")[0]
    return float(value)
df["rate"] = df["rate"].apply(Remove)
sns.barplot(x = "")

# Graph plot 
# plt.xlabel("Resturant Type")
# plt.ylabel("Rating")
# sns.barplot(x ="listed_in(type)", y = "rate", data=df, color="red")
# plt.show()