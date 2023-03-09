from dash import Dash
from dash import dcc,html
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from data import *
from dash import Input, Output, html



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

modal = html.Div(
    [
        dbc.Modal(
            [
                html.Div(id="image-show",style={"background-image": "linear-gradient(to bottom right,#FF69B4, #DC143C,#FF4500)","font-weight": "500","color":"#FFFAF0"
                                                              ,"font-size":"2rem","width":"33.5vw","text-aligh":"center"}),
            ],
            id="modal-centered",
            centered=True,
            is_open=False,style={"margin-left": "auto","margin-right": "auto","display": "block",}
        ),
    ],style={"width":"33.5vw"}
)
SIDEBAR_STYLE = {
    "top" : "8rem",
    "width": "30%",
    "padding": "2rem 3rem 0 3rem",
    "background-image": "linear-gradient(to bottom, #FEE1E8, #ffcaa3,#ff9999)",
    "float":"left",
    "height": "135vh",
}

CONTENT_STYLE = {
    "top":0,
    "height" : "8rem",
    "padding": "2rem 0",
    "background-image": "linear-gradient(to bottom right,#FF69B4, #DC143C,#FF4500)",
    "width" : "100.7%",

}
cog = html.Div(className="fa-sharp fa-solid fa-gear",style={"margin": "0 5px"})

sex = html.Div(className="fa-solid fa-venus-mars",style={"margin": "0 5px"})

course = html.Div(className="fa-solid fa-book",style={"margin": "0 5px"})

graduate = html.Div(className="fa-solid fa-graduation-cap",style={"margin": "0 5px"})

school = html.Div(className="fa-solid fa-school",style={"margin": "0 5px"})

passport = html.Div(className="fa-solid fa-passport",style={"margin": "0 5px"})

money = html.Div(className="fa-regular fa-money-bill-1",style={"margin": "0 5px"})

family = html.Div(className="fa-solid fa-heart",style={"margin": "0 5px"})

input_box = {"font-weight": "500","background-image": "linear-gradient(#FFA07A, #ff4000)","color":"#FFFAF0","border-color": "#ff8c66"}
sidebar = html.Div(
    [   html.Div(
            children=[
                html.H2(
                    children="YOUR INFORMATION",
                    style={
                        "textAlign": "center","font-weight": "bold",
                    },
                )
            ],
            className="row",style={ "padding": "1rem 0 1rem 0","width" : "100.7%"}
        ),
        html.P(children=[sex,"Select Your Gender"]
            ,className="lead",style={"font-weight": "500",}
        ),
        html.Div([
                dbc.Select(
                id="Gender-dd",
                options=[{"label": s, "value": s} for s in ['เพศชาย','เพศหญิง']], 
            ), ],style={"top": "20px;",
                        "margin": "0 0 4vh 0",
                             },
                    className="col-sm")
        ,
        html.P(children=[graduate,"Select Department"]
            , className="lead",style={"font-weight": "500",}
        ),
        html.Div([
                html.Div([
                dcc.Dropdown([s for s in DEPT_NAME_THAI if s != ""], 'ภาควิชาวิศวกรรมไฟฟ้า', id='Department-dd'),], 
            ),
                    ],style={"top": "20px;",
                             "margin": "0 0 4vh 0",
                             },
                    className="col-sm")
        ,    
                html.P(children=[course,"Select Major"]
            , className="lead",style={"font-weight": "500",}
        ),
        html.Div([dcc.Dropdown( id="Major-dd"),],style={"top": "20px;",
                             "margin": "0 0 4vh 0",
                             },
                    className="col-sm")
        ,    
        html.P(children=[school,"Select School"]
            , className="lead",style={"font-weight": "500",}
        ),
        html.Div([
                html.Div([
                dcc.Dropdown([s for s in PREV_INSTITUTION_NAME if s != ""], ' ', id='school-dropdown'),
            ]),
                    ],style={"top": "20px;",
                             "margin": "0 0 4vh 0",
                             },
                    className="col-sm")
        ,    
        html.P(children=[passport,"Select Entertainment Method"]
            , className="lead",style={"font-weight": "500",}
        ),
        html.Div([
                html.Div([
                dcc.Dropdown([s for s in ENT_METHOD_DESC if s != ""], ' ', id='ent-dropdown',clearable=False,style={"text-overflow": "ellipsis"}),
                
            ]),
                    ],style={"top": "20px;",
                             "margin": "0 0 4vh 0","text-overflow": "ellipsis"
                             },
                    className="col-sm")
                ,    
        html.P(children=[money,"Select Fundamental"]
            , className="lead",style={"font-weight": "500",}
        ),
        html.Div([
                dbc.Select(
                id="Fundamental-dd",
                options=[{"label": s, "value": s} for s in FUND_NAME_CODE  if s != ""], 
            ),
                    ],style={"top": "20px;",
                             "margin": "0 0 4vh 0",
                             },
                    className="col-sm")
                ,    
        html.P(children=[family,"Select Family Status (Dispensable)"]
            , className="lead",style={"font-weight": "500",}
        ),
        html.Div([
                dbc.Select(
                id="Family-dd",
                options=[{"label": s, "value": s} for s in PARENTS_MARRIED_NAME  if s != ""], 
            ),
                    ],style={"top": "20px;",
                             "margin": "5px 0 4vh 0",
                             },
                    className="col-sm")
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(children=[
                html.H1(
                    children=["PREDICT RETIREMENT",cog,],
                    style={
                        "textAlign": "center","color" : "#F0F8FF","font-size":"3rem" , "font-weight": "bold","margin-right" : 0
                    },
                ),
                html.Div(
                    children=["Name",dcc.Input(id="input1", type="text", placeholder="NAME", debounce=True,
                                        style={"margin":"0 0.5vw 0 1vw","width":"20vw","textAlign": "left","top":"5vh","float":"right"}),
                    ],style={"font-weight": "500","top":"-4.5rem","position":"relative","float":"right","textAlign": "right","color":"#FFFFF0"}
                ),
                html.Div(
                    children=["Student ID",dcc.Input(id="input2", type="text", placeholder="Student ID", debounce=True,
                                        style={"margin":"0 0.5vw 0 1vw","width":"20vw","textAlign": "left","top":"5vh","float":"right"}),
                    ],style={"font-weight": "500","top":"-3.5rem","position":"relative","float":"right","textAlign": "right","color":"#FFFFF0"}
                ),
                html.Div(
                    children=["ACCURACY OF MACHINE LEARNING : 90.36%"
                    ],style={"font-weight": "500","top":"-7.5rem","position":"relative","float":"left","textAlign": "left","color":"#FFFFF0","margin-left":"2vw"}
                ),
                html.Div(
                    children=["NAME OF MACHINE LEARNING : Logistic Regression"
                    ],style={"font-weight": "500","top":"-7.5rem","position":"relative","float":"left","textAlign": "left","color":"#FFFFF0","margin-left":"2vw"}
                ),
            ],
            className="row",id="page-content", style=CONTENT_STYLE)


app.layout = html.Div( 
    children=[
        html.Div([dcc.Location(id="url"),content ,sidebar, ]),
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 1 Term 1",style=input_box),
                dbc.Input(id="EnterGradeTerm11",placeholder="EnterGradeTerm 1 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 1 Term 2",style=input_box),
                dbc.Input(id="EnterGradeTerm12",placeholder="EnterGradeTerm 1 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "0 0 0 7vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 2 Term 1",style=input_box),
                dbc.Input(id="EnterGradeTerm21",placeholder="EnterGradeTerm 2 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 2 Term 2",style=input_box),
                dbc.Input(id="EnterGradeTerm22",placeholder="EnterGradeTerm 2 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "0 0 0 7vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 3 Term 1",style=input_box),
                dbc.Input(id="EnterGradeTerm31",placeholder="EnterGradeTerm 3 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 3 Term 2",style=input_box),
                dbc.Input(id="EnterGradeTerm32",placeholder="EnterGradeTerm 3 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "0 0 0 7vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 4 Term 1",style=input_box),
                dbc.Input(id="EnterGradeTerm41",placeholder="EnterGradeTerm 4 1", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                 dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("Grade Year 4 Term 2",style=input_box),
                dbc.Input(id="EnterGradeTerm42",placeholder="EnterGradeTerm 4 2", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5),
                
                ],style={"margin": "0 0 0 7vh"}),
            dbc.Row([
                dbc.Col([
                    dbc.InputGroup([
                dbc.InputGroupText("GPA From Old School",style=input_box),
                dbc.Input(id="GPA_School",placeholder="GPA School", type="number", min=0.00,max=4.00,step=0.01),
                ],
            className="mb-3"),],width=5,style={"margin-right": "5vh"}),
                html.Button("SUBMIT TO PREDICT", id="input-button", n_clicks=0,
                            style={"width":"25vw","height":"4vh","margin-left":"0.5vw","background-image": "linear-gradient(to bottom right,#FF69B4, #DC143C,#FF4500)",
                                   "font-weight": "bold","color" : "#F0F8FF","border-color": "#ff8c66"})
                ],style={"margin": "0 0 0 7vh"}),
            dbc.Row([
                html.Div(id='ent-output-container',style={"text-align":"center"}),
                html.Div(id='show',style={"text-align":"center","pading":"5px"}),
                html.Div( [dcc.Graph(id="graph"),], className="col-10",style={'margin-left':"5vw","margin-bottom":"5px"}),
                html.Div( [dcc.Graph(id="graph-past"),], className="col-10",style={'margin-left':"5vw"}),modal              
                ],style={"margin": "0 5vh"}),
        ],style={"left": "30%" , "padding": "5vh 2rem 0 2rem","right": 0, "width" : "69vw" ,"height" : "100vh","float":"right","height":"auto"}),
        
    ],style={"background-color": "#ff9999","float":"right","height":"auto"}
)

