import dash_bootstrap_components as dbc
from dash import Dash, html
from data import *

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Statistics of Road Traffic Fatalities in 2554-2565",
                    style={
                        "textAlign": "center",
                    },
                )
            ],
            className="row",
        ),
    ],
)