#Import all the necessary libraries
from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

#Import and potentially clean the data
data1 = pd.read_csv("CSV_files/wins_per_team.csv")
data2 = pd.read_csv("CSV_files/wins_per_team.csv")

data1.sort_values("%W", inplace=True)
data2.sort_values("%D", inplace=True)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Team analysis",),
        html.P(
            children="Analyse the premier league data"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data1["Team"],
                        "y": data1["%W"],
                        "type":"scatter",
                    },
                ],
                "layout": {"title":"Premier league Win rate of teams",
                           'xaxis':{
                               'title':"Team"},
                            'yaxis':{
                                'title':"Percent Win Rate (%)"
                            }
                           }
            }
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data2["Team"],
                        "y": data2["%D"],
                        "type":"scatter",

                    },
                ],
                "layout": {"title":"Premier league draw rate of teams",
                           'xaxis':{
                               'title':"Team"},
                            'yaxis':{
                                'title':"Percent Draw Rate (%)"
                            }
                           }
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)