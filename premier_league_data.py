import pandas as pd
import seaborn as sns
import sqlite3 as sql
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

data_pd = pd.read_csv(r"PremierLeague_data\results.csv", parse_dates=True, encoding='ISO-8859-1')
data = pd.DataFrame(data_pd)

#print(data.iloc[0,:])
#print(data.loc[:, ['HomeTeam', 'FTHG', 'FTAG', 'AwayTeam']]) #FORMAT TO HAVE HOME TEAM, HOMEGOAL, AWAYGOAL, AWAYTEAM

#this shows when a team was winning at half time and then lost at half-time
#print(data.loc[(data.AwayTeam == 'Liverpool') & (data.FTR == 'A') & (data.HTR == 'H')])

#print(data.loc[data.FTAG.isin([8])])
#print(data.loc[data.FTHG.isin([5, 6, 7, 8, 9]) & data.FTAG.isin([2, 3, 4, 5, 6, 7])])
#print(list(data.columns))


# first_query = """
#     SELECT Season, DateTime, HomeTeam, FTHG, FTAG, AwayTeam
#     FROM prem_data
#     WHERE (HomeTeam = 'Liverpool' and AwayTeam = 'Man United') or ((HomeTeam = 'Man United' and AwayTeam = 'Liverpool'))
#     ORDER BY DateTime
# """
# second_query = """
#     SELECT Season, DateTime, HomeTeam, FTHG, FTAG, AwayTeam
#     FROM prem_data
#     WHERE Season = '2020-21'
#     ORDER BY DateTime
# """

third_query = """
    SELECT Season, SUM(HR), SUM(AR)
    FROM prem_data
    GROUP By Season
"""

#FETCHING AND ASSIGNING THE DATA
# cursor.execute(first_query)
# cursor.execute(second_query)
#cursor.execute(third_query)
# first_results = cursor.fetchmany()
# second_results = cursor.fetchall()
#third_results = cursor.fetchall()

#CONVERTING THE SQL DATA TO A PANDA DATAFRAME SO IT CAN BE USED TO VISUALISE ETC
# first_processed_data = pd.DataFrame(first_results, columns=['Season', 'DateTime', 'Home Team','HG','AG','Away Team'])
# second_processed_data = pd.DataFrame(second_results, columns=['Season', 'DateTime', 'HomeTeam', 'HG', 'AG', 'AwayTeam'])
# third_processed_data = pd.DataFrame(third_results, columns = ['Season', 'Yellows', 'Reds'])
# print(third_processed_data)

# graph_figure = sns.lineplot(data=third_processed_data)
# graph_figure.figure.savefig('graph.png')

def database_creator(db_Name):
    engine = create_engine(f'sqlite:///{db_Name}.db', echo=True)
    data.to_sql(db_Name, con=engine, if_exists='replace', index=False)
    open_connection = sql.connect(f'C:\\Users\\alexp\\Desktop\\Code\\Data Practice\\{db_Name}.db')
    cursor = open_connection.cursor()

    return cursor, open_connection

def database_closer(db_Name, cursor, connection):
    cursor.close()
    connection.close()

def SQL_query():
    pass

def graph_plotter (queryName, graphColumns, graphOut, cursor):
    cursor.execute(queryName)
    result = cursor.fetchall()

    #WRITE TO A DATA FRAME
    processed_data = pd.DataFrame(result, columns = graphColumns)

    #OUTPUT TO A GRAPH
    graph_figure = sns.lineplot(data=processed_data)
    graph_figure.figure.savefig(graphOut)

new_query = ['Season', 'Home Red', 'Away Red']

graph_plotter(third_query, new_query, 'RedCard stats')


# #for i in range (len(second_processed_data)):
#     HomeTeam = second_processed_data.Hom

#PRINT OF RESULTS TO CHECK THAT THE CORRECT DATA HAS COME OUT
# print(first_processed_data.head())
# print(second_processed_data.head(), second_processed_data.shape, second_processed_data.size)

#Allows us to close a connection when needed
