from layout import *
from dash import Input, Output,ctx,html,State
import pandas as pd
from pycaret.classification import *
import plotly.express as px
import random 

model = load_model("engipremo")

@app.callback(
    Output('ent-output-container', 'children'),
    Output("image-show","children"),
    [Input('input-button','n_clicks'),
     Input('Gender-dd', 'value'),
     Input('Major-dd', 'value'),
     Input('Department-dd', 'value'),
     Input('school-dropdown', 'value'),
     Input('ent-dropdown', 'value'),
     Input('Fundamental-dd', 'value'),
     Input('Family-dd', 'value'),
     Input('EnterGradeTerm11', 'value'),
     Input('EnterGradeTerm12', 'value'),
     Input('EnterGradeTerm21', 'value'),
     Input('EnterGradeTerm22', 'value'),
     Input('EnterGradeTerm31', 'value'),
     Input('EnterGradeTerm32', 'value'),
     Input('EnterGradeTerm41', 'value'),
     Input('EnterGradeTerm42', 'value'),
     Input('GPA_School', 'value'),
     ]
)
def update_output(n_clicks,gen,maj,dep,sch,ent,fun,fam,t11,t12,t21,t22,t31,t32,t41,t42,gpa):
    text = "Please Enter Your Information"
    text_style = {"font-weight": "bold","color":"#000000","font-size": "2.5em"}
    ran = random.randrange(0,3)
    show_img = [html.Img(src="https://drive.google.com/uc?export=download&id=1I3BlgKcpxEZUQRXBCa4h_jmGGOgywT1w", alt='image',
                         style={"display": "block","margin-left": "auto","margin-right": "auto",
                                "width":"33.5vw","height":"auto"}),
                html.Div("HMM? Please Check Your Information"),]
    if 'input-button' == ctx.triggered_id :
        if gen not in ['เพศชาย','เพศหญิง']:
            text =  "Please Select Your Gender"
        elif maj not in MAJOR_NAME_THAI :
            text = "Please Select Your Major"
        elif dep not in DEPT_NAME_THAI:
            text = "Please Select Your Departmnet"
        elif sch is None:
            text = "Please Select Your Old School"
        elif ent is None:
            text = "Please Select Your Entertainment Method"
        elif fun not in FUND_NAME_CODE:
            text = "Please Select Your Fundamental"
        elif gpa is None :
            text = "Please Enter Your GPA"
        elif t11 is None :
            text = "Please Enter Your Grade, At Least Grade Year 1 Term 1"
        else:
            you = {"MAJOR_NAME_THAI":[maj],"DEPT_NAME_THAI":[dep],"SEX_NAME_THAI":[gen],
                "ENT_METHOD_DESC":[ent],"PREV_INSTITUTION_NAME":[sch],
                "เกรดปี1เทอม1":[t11],"เกรดปี1เทอม2":[t12],
                "เกรดปี2เทอม1":[t21],"เกรดปี2เทอม2":[t22],
                "เกรดปี3เทอม1":[t31],"เกรดปี3เทอม2":[t32],
                "เกรดปี4เทอม1":[t41],"เกรดปี4เทอม2":[t42],
                "GPA_SCHOOL":[gpa],"FUND_NAME_CODE":[fun],"PARENTS_MARRIED_NAME":[fam]}
            new_data = pd.DataFrame(you)
            predictiions = predict_model(model,new_data)
            predic = predictiions["prediction_label"]
            if predic[0] == "ตกออก (พ้นสภาพการเป็นนักศึกษา)":
                text_style = {"font-weight": "bold","color":"#ff0000","font-size": "2.5em"}
                text = "OH NO, BE CAREFUL!"
                show_img = [html.Img(src=fail[ran], alt='image',style={"display": "block","margin-left": "auto","margin-right": "auto","width":"33.5vw","height":"auto"}),html.Div(text),]
            else :
                text_style = {"font-weight": "bold","color":"#228B22","font-size": "2.5em"}
                text = "CONGRATULATIONS!"
                show_img = [html.Img(src=past[ran], alt='image',style={"display": "block","margin-left": "auto","margin-right": "auto","width":"33.5vw","height":"auto"}),html.Div(text),]
    return html.Div(text,style=text_style),show_img


@app.callback(
    Output('show', 'children'),
    [Input('input-button','n_clicks'),
     Input('Gender-dd', 'value'),
     Input('Major-dd', 'value'),
     Input('Department-dd', 'value'),
     Input('school-dropdown', 'value'),
     Input('ent-dropdown', 'value'),
     Input('Fundamental-dd', 'value'),
     Input('Family-dd', 'value'),
     Input('EnterGradeTerm11', 'value'),
     Input('EnterGradeTerm12', 'value'),
     Input('EnterGradeTerm21', 'value'),
     Input('EnterGradeTerm22', 'value'),
     Input('EnterGradeTerm31', 'value'),
     Input('EnterGradeTerm32', 'value'),
     Input('EnterGradeTerm41', 'value'),
     Input('EnterGradeTerm42', 'value'),
     Input('GPA_School', 'value'),
     ]
)
def update_output(n_clicks,gen,maj,dep,sch,ent,fun,fam,t11,t12,t21,t22,t31,t32,t41,t42,gpa):
    text = "Your Prediction Will Show Here"
    text_style = {"font-weight": "bold","color":"#000000","font-size": "1em"}
    if 'input-button' == ctx.triggered_id :
        if gen not in ['เพศชาย','เพศหญิง']:
            text =  "Your Prediction Will Show Here"
        elif maj not in MAJOR_NAME_THAI :
            text = "Your Prediction Will Show Here"
        elif dep not in DEPT_NAME_THAI:
            text = "Your Prediction Will Show Here"
        elif sch is None:
            text = "Your Prediction Will Show Here"
        elif ent is None:
            text = "Your Prediction Will Show Here"
        elif fun not in FUND_NAME_CODE:
            text = "Your Prediction Will Show Here"
        elif gpa is None :
            text = "Your Prediction Will Show Here"
        elif t11 is None :
            text = "Your Prediction Will Show Here"
        else:
            you = {"MAJOR_NAME_THAI":[maj],"DEPT_NAME_THAI":[dep],"SEX_NAME_THAI":[gen],
                "ENT_METHOD_DESC":[ent],"PREV_INSTITUTION_NAME":[sch],
                "เกรดปี1เทอม1":[t11],"เกรดปี1เทอม2":[t12],
                "เกรดปี2เทอม1":[t21],"เกรดปี2เทอม2":[t22],
                "เกรดปี3เทอม1":[t31],"เกรดปี3เทอม2":[t32],
                "เกรดปี4เทอม1":[t41],"เกรดปี4เทอม2":[t42],
                "GPA_SCHOOL":[gpa],"FUND_NAME_CODE":[fun],"PARENTS_MARRIED_NAME":[fam]}
            new_data = pd.DataFrame(you)
            predictiions = predict_model(model,new_data)
            predic = predictiions["prediction_label"]
            score = predictiions["prediction_score"]
            per = "{:.2f}%".format(score[0]*100)
            if predic[0] == "ตกออก (พ้นสภาพการเป็นนักศึกษา)":
                text_style = {"font-weight": "bold","color":"#ff0000","font-size": "1em"}
                text = " คุณมีโอกาส"+"ตกออก "+per
            else :
                text_style = {"font-weight": "bold","color":"#228B22","font-size": "1em"}
                text = " คุณมีโอกาส"+"สำเร็จการศึกษา "+per
    return html.Div(text,style=text_style)

@app.callback(
    Output('graph', 'figure'),
    [Input('input-button','n_clicks'),
     Input('Major-dd', 'value'),
     Input('Department-dd', 'value'),
     ]
)
def update_output(n_clicks,maj,dep):
    fig = px.strip(None,y=None,template='ggplot2',title="กราฟแสดงตัวอย่างเกรดจะปรากฏที่นี่")
    if 'input-button' == ctx.triggered_id :
        df1 = df
        df1 = df1[df1["STATUS_DESC_THAI"] == "สำเร็จการศึกษา (พ้นสภาพการเป็นนักศึกษา)"]
        df1 = df1[df1["MAJOR_NAME_THAI"] == maj]
        df1 = df1[df1["DEPT_NAME_THAI"] == dep]
        df1 = df1[df1["เกรดปี1เทอม1"] > 1.25]
        df1 = df1[df1["เกรดปี1เทอม2"] > 1.25]
        df1 = df1[df1["เกรดปี2เทอม1"] > 1.25]
        df1 = df1[df1["เกรดปี2เทอม2"] > 1.25]
        df1 = df1[df1["เกรดปี3เทอม1"] > 1.25]
        df1 = df1[df1["เกรดปี3เทอม2"] > 1.25]
        df1 = df1[df1["เกรดปี4เทอม1"] > 1.25]
        df1 = df1[df1["เกรดปี4เทอม2"] > 1.25]
        fig = px.strip(df1,  y=['เกรดปี1เทอม1',	'เกรดปี1เทอม2'	,'เกรดปี2เทอม1'	,'เกรดปี2เทอม2'	,'เกรดปี3เทอม1',	'เกรดปี3เทอม2',	'เกรดปี4เทอม1',	'เกรดปี4เทอม2'],template='ggplot2',
                       title="ตัวอย่างเกรดของนักศึกษาที่สำเร็จการศึกษา {} {}".format(maj,dep))
    return fig


@app.callback(
    Output('Major-dd', 'options'),
    Input('Department-dd', 'value'),
)
def update_output(dep):
    new_major = df[df["DEPT_NAME_THAI"] == dep]
    new_list = [s for s in new_major["MAJOR_NAME_THAI"].unique() if s != ""]
    return new_list 


@app.callback(
    Output("modal-centered", "is_open"),
    Input('input-button', "n_clicks"),
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)
