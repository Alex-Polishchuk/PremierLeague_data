from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv("CSV_files/wins_per_team.csv")
print(data.head())

data = data.query("Team == 'Arsenal'")

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
                        "type":"lines",
                    },
                ],
                "layout": {"title":"Premier league data"}
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)