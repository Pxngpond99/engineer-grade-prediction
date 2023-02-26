import dash_bootstrap_components as dbc
from dash import Dash, html
from data import *

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Mechine Learning",
                    style={
                        "left" : "0vw" , "padding-left" : "3vh","color" : "#F8F8FF" ,"margin": "0","height":"13vh"
                    },
                )
           
            ], style={"background-color" : "#000000"},
        ),
        html.Div(
            children=[
                html.H1(
                    children="Mechine Learning For Prediction Grade",
                    style={
                        "textAlign": "center","background-color" : "#D3D3D3","margin": "0 5vw","bottom": "0px","height":"87vh"
                    },
                )
            ],
        ),
    ],style={"height":"100vh"}
)