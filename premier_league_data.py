import pandas as pd
import seaborn as sb
import sqlite3 as sql
from sqlite3 import Error
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


data_pd = pd.read_csv('results.csv', parse_dates=True)
data = pd.DataFrame(data_pd)

#print(data.iloc[0,:])
#print(data.loc[:, ['HomeTeam', 'FTHG', 'FTAG', 'AwayTeam']]) #FORMAT TO HAVE HOME TEAM, HOMEGOAL, AWAYGOAL, AWAYTEAM

#this shows when a team was winning at half time and then lost at half-time
#print(data.loc[(data.AwayTeam == 'Liverpool') & (data.FTR == 'A') & (data.HTR == 'H')])

#print(data.loc[data.FTAG.isin([8])])
#print(data.loc[data.FTHG.isin([6, 7, 8, 9]) & (data.HomeTeam == 'Liverpool')])
#print(list(data.columns))

#engine = create_engine('sqlite:///prem_data.db', echo=True)
#data.to_sql('prem_data', con=engine, if_exists='replace', index=False)
open_connection = sql.connect('C:\\Users\\alexp\\Desktop\\Code\\Data Practice\\prem_data.db')
cursor = open_connection.cursor()

query = """
    SELECT HomeTeam
    FROM prem_data
    WHERE AwayTeam = 'Liverpool' and  FTR = 'H'
"""

cursor.execute(query)
results = cursor.fetchall()

print(results)



###CREATING AN SQL QUERY TO CREATE A DATA frame | 1. create the query and save to dataframe. 2. create a name for the file. 3. save the file and create a plot 


#Allows us to close a connection when needed
cursor.close()
open_connection.close()