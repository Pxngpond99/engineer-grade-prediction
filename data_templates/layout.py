import dash_bootstrap_components as dbc
from dash import Dash, html
from data import *

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Mechine Learning For Prediction Grade",
                    style={
                        "textAlign": "center",
                    },
                )
            ],
        ),
    ],
)