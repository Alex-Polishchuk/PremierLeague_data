#Import all the necessary libraries
from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

#Import and potentially clean the data
data = pd.read_csv("CSV_files/wins_per_team.csv")
data.sort_values("%W", inplace=True)

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
                        "x": data["Team"],
                        "y": data["%W"],
                        "type":"scatter",
                    },
                ],
                "layout": {"title":"Premier league data", "x":"Win Percentage (%)", "y":"Teams"}
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)