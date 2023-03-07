from dash import Dash
from dash import dcc,html
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import *
from dash import Input, Output, html



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top" : "8rem",
    "bottom": 0,
    "width": "30vw",
    "padding": "5rem 3rem",
    "background-color": "#FEE1E8",
}

CONTENT_STYLE = {
    "height" : "8rem",
    "padding": "2rem 0",
    "background-image": "linear-gradient(to bottom right,#FF69B4, #DC143C,#FF4500)",
    "width" : "100.7%",
    "margin-right" : 0
}
cog = html.Div(className="fa-sharp fa-solid fa-gear",style={"margin": "0 5px"})

sex = html.Div(className="fa-solid fa-venus-mars",style={"margin": "0 5px"})

course = html.Div(className="fa-solid fa-book",style={"margin": "0 5px"})

graduate = html.Div(className="fa-solid fa-graduation-cap",style={"margin": "0 5px"})

school = html.Div(className="fa-solid fa-school",style={"margin": "0 5px"})

passport = html.Div(className="fa-solid fa-passport",style={"margin": "0 5px"})

money = html.Div(className="fa-regular fa-money-bill-1",style={"margin": "0 5px"})

family = html.Div(className="fa-solid fa-heart",style={"margin": "0 5px"})

sidebar = html.Div(
    [
        html.P(children=[sex,"Select Your Gender"]
            ,className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Gender-dd",
                options=[{"label": s, "value": s} for s in ['เพศชาย','เพศหญิง']], 
            ), ],style={"top": "20px;",
                        "margin": "0 0 10px 0",
                             },
                    className="col-sm")
        ,
        html.P(children=[course,"Select Major"]
            , className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Major-dd",
                options=[{"label": s, "value": s} for s in MAJOR_NAME_THAI], 
            ),
                    ],style={"top": "20px;",
                             "margin": "0 0 10px 0",
                             },
                    className="col-sm")
        ,    
        html.P(children=[graduate,"Select Department"]
            , className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Department-dd",
                options=[{"label": s, "value": s} for s in DEPT_NAME_THAI], 
            ),
                    ],style={"top": "20px;",
                             "margin": "0 0 10px 0",
                             },
                    className="col-sm")
        ,    
        html.P(children=[school,"Select School"]
            , className="lead"
        ),
        html.Div([
                html.Div([
                dcc.Dropdown([s for s in PREV_INSTITUTION_NAME if s != ""], ' ', id='school-dropdown'),
                html.Div(id='school-output-container')
            ]),
                    ],style={"top": "20px;",
                             "margin": "0 0 10px 0",
                             },
                    className="col-sm")
        ,    
        html.P(children=[passport,"Select Entertainment Method"]
            , className="lead"
        ),
        html.Div([
                html.Div([
                dcc.Dropdown([s for s in ENT_METHOD_DESC if s != ""], ' ', id='ent-dropdown'),
                html.Div(id='ent-output-container')
            ]),
                    ],style={"top": "20px;",
                             "margin": "0 0 10px 0",
                             },
                    className="col-sm")
                ,    
        html.P(children=[money,"Select Fundamental"]
            , className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Fundamental-dd",
                options=[{"label": s, "value": s} for s in FUND_NAME_CODE  if s != ""], 
            ),
                    ],style={"top": "20px;",
                             "margin": "0 0 10px 0",
                             },
                    className="col-sm")
                ,    
        html.P(children=[family,"Select Family Status"]
            , className="lead"
        ),
        html.Div([
                dbc.Select(
                id="Family-dd",
                options=[{"label": s, "value": s} for s in PARENTS_MARRIED_NAME  if s != ""], 
            ),
                    ],style={"top": "20px;",
                             "margin": "5px 0 10px 0",
                             },
                    className="col-sm")
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(children=[
                html.H1(
                    children=["PREDICT RETIREMENT",cog],
                    style={
                        "textAlign": "center","color" : "#F0F8FF","font-size":"3rem" , "font-weight": "bold","margin-right" : 0
                    },
                )
            ],
            className="row",id="page-content", style=CONTENT_STYLE)


app.layout = html.Div( 
    children=[
        html.Div([dcc.Location(id="url"), sidebar, content]),
        html.Div(
            
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
            className="row",style={ "padding": "1rem 0 4rem 0","width" : "100.7%"}
        ),
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 1 Term 1"),
                dbc.Input(id="EnterGradeTerm11",placeholder="EnterGradeTerm 1 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 1 Term 2"),
                dbc.Input(id="EnterGradeTerm12",placeholder="EnterGradeTerm 1 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "0 5vh 5vh 5vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 2 Term 1"),
                dbc.Input(id="EnterGradeTerm21",placeholder="EnterGradeTerm 2 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 2 Term 2"),
                dbc.Input(id="EnterGradeTerm22",placeholder="EnterGradeTerm 2 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "5vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 3 Term 1"),
                dbc.Input(id="EnterGradeTerm31",placeholder="EnterGradeTerm 3 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 3 Term 2"),
                dbc.Input(id="EnterGradeTerm32",placeholder="EnterGradeTerm 3 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "5vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 4 Term 1"),
                dbc.Input(id="EnterGradeTerm41",placeholder="EnterGradeTerm 4 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 4 Term 2"),
                dbc.Input(id="EnterGradeTerm42",placeholder="EnterGradeTerm 4 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "5vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("GPA From Old School"),
                dbc.Input(id="GPA_School",placeholder="GPA School", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                dbc.Button("SUNMIT TO PREDICT", id="input-button", n_clicks=0)
            ],style={"margin": "5vh"})
        ],style={"marginLeft": "30vw" , "padding": "0 2rem","right": 0, "width" : "69vw",})
    ],style={"background-color": "#ff9999","height":"98vh"}
)