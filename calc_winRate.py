#to calculate the win rate of teams (overall, per season, against certain teams)

import pandas as pd
import seaborn as sns
import sqlite3 as sql
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

df = pd.read_csv('results.csv', parse_dates=True)

#Calculating win rates for teams

#Creating a dataframe for team

#add all teams to dataFrame

home_value = df.value_counts('HomeTeam')
away_value = df.value_counts('AwayTeam')

#convertings values to a dataframe
home_df = pd.DataFrame(home_value)
away_df = pd.DataFrame(away_value)

#renaming columns for clarity
home_df = home_df.rename(columns={0:'Games Played Home'})
away_df = away_df.rename(columns={0:'Games Played Away'})

#resetting index
home_df.reset_index(inplace=True)
away_df.reset_index(inplace=True)

#renaming columns
home_df = home_df.rename(columns={'HomeTeam':'Team'})
away_df = away_df.rename(columns={'AwayTeam':'Team'})

#merging two dataframes together
total_df = pd.merge(home_df, away_df, on='Team')
print(home_df.shape, total_df.shape, away_df.shape)

total_df['Total Played'] = ''

total_df.loc[total_df['Liverpool']] = 10

print(total_df)

for index, team in total_df.iterrows():
    filter = total_df.loc[total_df['Team'] == team['Team']]
    home_played = filter['Games Played Home']
    home_played = int(home_played)
    away_played = filter['Games Played Away']
    away_played = int(away_played)
    total_played = home_played + away_played
    #print(type(total_played))

print(total_df)