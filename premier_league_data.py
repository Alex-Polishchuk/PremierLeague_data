import pandas as pd
import seaborn as sns
import sqlite3 as sql
from sqlalchemy import create_engine

data_pd = pd.read_csv("results.csv", parse_dates=True, encoding='ISO-8859-1')

#Data is saved to a pandas data frame
data = pd.DataFrame(data_pd)

string = """
SELECT *
FROM prem_data.db
"""

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

def process_data(output_name, cursor, query):
    try:
        cursor.execute(query)
        output_name = cursor.fetchall()
    except:
        print("An error has occured with your query")
    
    return output_name

def query_acceptor():
    user_input = input(str("Input your search query:\n"))
    return user_input

def sql_to_DF(query, DF_name):
    print("SQL to DataFrame")
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

name = "prem_data"

if __name__ == "__main__":
    cursor, open_connecction = database_creator(name)
    #user_query = query_acceptor()
    data = process_data("SQL_output", string, cursor)
    DF = sql_to_DF(data, "dataframe_test")
    database_closer(name, cursor, open_connecction)
