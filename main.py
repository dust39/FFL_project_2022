import pandas as pd

import matplotlib.pyplot as plt

import sys

msg="Welcome to my Python Fantasy Football Project 2022"
print(msg)

def getuserinput():
    year=input("Hello, please enter a four digit year from 1970 to 2019 to see the top 10 fantasy scorers from that year!")
    converted_num=int(year)
    if converted_num in range(1970,2020,1):
       return(year)
    else:
        while converted_num not in range(1970,2020,1): 
            year=input("Please try again. Please enter a valid 4 digit year between 1970 and 2019. Type 'end' to quit.")
            if year == "end" or year == "'end'":                
                sys.exit()
            converted_num=int(year)
        else:
            return(year)   

desired_year=getuserinput()

df1=pd.read_csv("project_data/yearly/"+desired_year+".csv")

df1.sort_values("FantasyPoints", ascending=False)
df1.drop(['Unnamed: 0'],axis=1,inplace=True)

player_name_list=(df1["Player"]+"-"+df1["Pos"]).tolist()

player_initial_list=[]

for name in player_name_list:
    first_initial= name[0]+"."
    name_separation_index=name.find(" ")
    last_name=name[name_separation_index+1:]
    player_initial_list.append(first_initial+last_name)

df1["1stInitial_LastName"]=player_initial_list

df2 = df1.nlargest(n=10,columns="FantasyPoints")

plt.figure(figsize=(11,8))
plt.bar(x=df2["1stInitial_LastName"], height=df2["FantasyPoints"])
plt.ylabel('Total Fantasy Points', fontsize=18)
plt.xlabel('Player', fontsize=18)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xticks(rotation = 45)
plt.savefig("jpg_output\Bargraph_Output"+desired_year+".jpg")
plt.show()
