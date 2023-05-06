import pandas as pd
import seaborn as sns
import sqlite3 as sql
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

data_pd = pd.read_csv("results.csv", parse_dates=True, encoding='ISO-8859-1')

#Data is saved to a pandas data frame
data = pd.DataFrame(data_pd)

#create a databse with a specified name
def database_creator(db_Name):
    engine = create_engine(f'sqlite:///{db_Name}.db', echo=True)
    data.to_sql(db_Name, con=engine, if_exists='replace', index=False)
    open_connection = sql.connect(f'C:\\Users\\alexp\\Desktop\\Code\\Data Practice\\{db_Name}.db')
    cursor = open_connection.cursor()

    return cursor, open_connection
    #returns cursor which interacts with the database created
    #returns the connection, this is so it can be closed in the future

def database_closer(db_Name, cursor, connection):
    cursor.close()
    connection.close()

def SQL_query():
    #creates a SQL query?
    pass

def SQL_exec():
    pass

def graph_plotter (queryName, graphColumns, graphOut, cursor):
    cursor.execute(queryName)
    result = cursor.fetchall()

    #WRITE TO A DATA FRAME
    processed_data = pd.DataFrame(result, columns = graphColumns)

    #OUTPUT TO A GRAPH
    graph_figure = sns.lineplot(data=processed_data)
    graph_figure.figure.savefig(graphOut)

def remove_data(data, *args):
    for i in args:
        data = data.drop(i, axis=1)
    return data

def process_data(output_name, cursor, query):
        
    cursor.execute(query)
    output_name = cursor.fetchall()
    return output_name

#DELETS uncomplete data in the season, showcase this before hand
delete_query = """
    DELETE
    FROM prem_data
    WHERE season = 2021-22
"""
name = "prem_data"
cursor, open_connecction = database_creator(name)
print(data)



database_closer(name, cursor, open_connecction)

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

#graph_plotter(third_query, new_query, 'RedCard stats')

