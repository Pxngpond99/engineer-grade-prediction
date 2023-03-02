from dash import Dash
from dash import dcc,html
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import *
from dash import Input, Output, html

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#FEE1E8",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "5rem 3rem",
}

sidebar = html.Div(
    [
        html.H2("SelectBar", className="display-4"),
        html.Hr(),
        html.P(
            "Select Your Gender", className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Gender",
                options=[{"label": s, "value": s} for s in ['เพศชาย','เพศหญิง']], 
            ), ],style={"top": "20px;",
                        "margin": "5px 5px 5px 5px",
                             },
                    className="col-sm")
        ,
        html.P(
            "Select Course Degree", className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Department",
                # value=df["COURSE_DEGREE"],
                options=[{"label": s, "value": s} for s in df["MAJOR_NAME_THAI"].unique()], 
            ),
                    ],style={"top": "20px;",
                             "margin": "5px 5px 5px 5px",
                             },
                    className="col-sm")
        ,    
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)


app.layout = html.Div( 
    children=[
        html.Div([dcc.Location(id="url"), sidebar, content]),
        html.Div(
            children=[
                html.H1(
                    children="Predict Retirement",
                    style={
                        "textAlign": "center",
                    },
                )
            ],
            className="row",
        ),
        html.Div(
            children=[
                html.H2(
                    children="Enter your information",
                    style={
                        "textAlign": "center",
                    },
                )
            ],
            className="row",
        ),
        # html.Div(
        #     children=[
        #         html.Div([
        #         dcc.Dropdown(
        #                     options=[x for x in df["COURSE_DEGREE"].unique()],
        #                     value=df["COURSE_DEGREE"].min(),
        #                     id='dd-output-container',clearable=True,
        #                     style={}
        #                 )
        #             ],style={"top": "20px;","margin": "0 30vw 10px 30vw",},
        #             className="col-sm")
        #     ]
        # )
        # ,
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm11"),
                dbc.Input(placeholder="EnterGradeTerm11", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm12"),
                dbc.Input(placeholder="EnterGradeTerm12", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                
                ]),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm21"),
                dbc.Input(placeholder="EnterGradeTerm21", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm22"),
                dbc.Input(placeholder="EnterGradeTerm22", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                
                ]),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm31"),
                dbc.Input(placeholder="EnterGradeTerm31", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm32"),
                dbc.Input(placeholder="EnterGradeTerm32", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                
                ]),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm41"),
                dbc.Input(placeholder="EnterGradeTerm41", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("EnterGradeTerm42"),
                dbc.Input(placeholder="EnterGradeTerm42", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=6),
                
                ]),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("GPA_School"),
                dbc.Input(placeholder="GPA_School", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-20"),],width=6),
            ])
        ])
    ],style={"marginLeft": 275}
)
