
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msg="Welcome to my Python Fantasy Football Project 2022"
print(msg)


df1=pd.read_csv("project_data/yearly/2019.csv")
df1.sort_values("FantasyPoints", ascending=False)
#this drops my extra indexing column
df1.drop(['Unnamed: 0'],axis=1,inplace=True)



#this takes my data frame column Player and makes it a list so that I can extract 1st initial last name below.
player_name_list=df1["Player"].tolist()
#prints player list
# print(player_name_list)


#initializes an empty list so I can add new list with Player first initial and last name.
player_initial_list=[]
#for loop to iterate over player name list
for name in player_name_list:
    # uses slicing to grab index 0 of string, which is the first letter of the first name, then adds . after
    first_initial= name[0]+"."
    # this uses the str.find function to find at which index the space between first and last name is
    name_separation_index=name.find(" ")
    #this uses slicing to return (value of index of the empty space between names+1) plus returns rest of string after that
    last_name=name[name_separation_index+1:]
    #this combines the first initial and last name via concatenation then it adds the new string to list "player_initial_list"
    player_initial_list.append(first_initial+last_name)
    #this prints the list so that I can be sure the list shows as I expect
    #print(player_initial_list)


#print(player_initial_list)


#adds a column to the data fram
#series=pd.Series(player_initial_list)
df1["1st_Initial,LastName"] =np.array(player_initial_list)



df1.head(5)


df1.describe()


df1.shape


df1.dtypes


print(df1.describe())


df2 = df1.nlargest(n=10,columns="FantasyPoints")
df2.head(5)




# plot specifications. worth noting plt.figure needs to go first and savefig for jpg output needs to go near end
plt.figure(figsize=(11,8))

plt.bar(x=df2["1st_Initial,LastName"], height=df2["FantasyPoints"])
plt.ylabel('Total Fantasy Points', fontsize=18)
plt.xlabel('Player', fontsize=18)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xticks(rotation = 45)
plt.savefig("Bar_Output.jpg")
plt.show()