import pandas as pd
import numpy as np

df = pd.read_csv("Football Manager/fifa_processed.csv")

def rank_players(pos, country, age, sortby):
    df_smaller = df
    
    if pos != "Any":
        df_smaller = df_smaller.loc[df["Pos_simp"] == pos]
    if country != "Any":
        df_smaller = df_smaller.loc[df["Nationality"] == country]
    if age != "Any":
        if age == "Below 18":
            df_smaller = df_smaller.loc[df["Age"] < 18]
        if age == "18-21":
            df_smaller = df_smaller.loc[(df["Age"] >= 18) & (df["Age"] < 22)]
        if age == "22-26":
            df_smaller = df_smaller.loc[(df["Age"] >= 22) & (df["Age"] < 27)]
        if age == "27-31":
            df_smaller = df_smaller.loc[(df["Age"] >= 27) & (df["Age"] < 32)]
        if age == "Above 31":
            df_smaller = df_smaller.loc[(df["Age"] > 31)]
    
    df_smaller = df_smaller.sort_values(by = [sortby], ascending = False).head(10)
    df_smaller = df_smaller[["Name", "Pos_simp", "Age", "Nationality", sortby]]
    if len(df_smaller) == 0:
        print("Sorry, no players match your criteria")
    else:
        print(df_smaller)


def man_mode(formation, age, country):
    
    df_smaller = df
    
    if country != "Any":
        df_smaller = df_smaller.loc[df["Nationality"] == country]
        
    if age != "Any":
        if age == "Below 18":
            df_smaller = df_smaller.loc[df["Age"] < 18]
        if age == "18-21":
            df_smaller = df_smaller.loc[(df["Age"] >= 18) & (df["Age"] < 22)]
        if age == "22-26":
            df_smaller = df_smaller.loc[(df["Age"] >= 22) & (df["Age"] < 27)]
        if age == "27-31":
            df_smaller = df_smaller.loc[(df["Age"] >= 27) & (df["Age"] < 32)]
        if age == "Above 31":
            df_smaller = df_smaller.loc[(df["Age"] > 31)]
            
    
    
    df_gk = df_smaller.loc[df_smaller["Pos_simp"] == "GK"]
    gk_list = df_gk.head(1)["Name"].tolist()
    
    df_def = df_smaller.loc[df_smaller["Pos_simp"] == "DEF"]
    n_def = int(formation.split("-")[0])
    def_list = df_def.head(n_def)["Name"].tolist()
    
    df_mid = df_smaller.loc[df_smaller["Pos_simp"] == "MID"]
    n_mid = int(formation.split("-")[1])
    mid_list = df_mid.head(n_mid)["Name"].tolist()
    
    df_st = df_smaller.loc[df_smaller["Pos_simp"] == "ATT"]
    n_st = int(formation.split("-")[2])
    st_list = df_st.head(n_st)["Name"].tolist()
    
    team_list = gk_list + def_list + mid_list + st_list
    return team_list
 

print(man_mode("4-4-2", "18-21", "France"))