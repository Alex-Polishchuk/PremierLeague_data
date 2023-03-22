import pandas as pd
import csv
import seaborn as sb
import sqlite3 as sql

data_pd = pd.read_csv('results.csv')
data = pd.DataFrame(data_pd)

#print(data.iloc[0,:])
#print(data.loc[:, ['HomeTeam', 'FTHG', 'FTAG', 'AwayTeam']]) #FORMAT TO HAVE HOME TEAM, HOMEGOAL, AWAYGOAL, AWAYTEAM

#this shows when a team was winning at half time and then lost at half-time
#print(data.loc[(data.HomeTeam == 'Arsenal') & (data.FTR == 'A') & (data.HTR == 'H')])

#print(data.loc[data.FTAG.isin([8])])
#print(data.loc[data.FTHG.isin([9])])

sql_data = sql.connect(data)
cursor = sql_data.cursor()

#pd.read_sql_query(query, sql_data)

sql_data.close()