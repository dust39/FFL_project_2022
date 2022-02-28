import pandas as pd
import matplotlib.pyplot as plt

msg="Welcome to my Python Fantasy Football Project 2022"
print(msg)

df1=pd.read_csv("data_v2/yearly/2019.csv")
df1.sort_values("FantasyPoints", ascending=False)


df2 = df1.nlargest(n=10,columns="FantasyPoints")
print(df2)

print(df1.describe())


plt.bar(x=df2["Player"], height=df2["FantasyPoints"])
plt.ylabel('Total Fantasy Points')
plt.xlabel('Player')
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)
plt.show()