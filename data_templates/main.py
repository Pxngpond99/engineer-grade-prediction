from layout import *
from dash import Input, Output
import pandas



@app.callback(
    Output('ent-output-container', 'children'),
    [Input('Gender-dd', 'value'),
     Input('Major-dd', 'value'),
     Input('Department-dd', 'value'),
     Input('school-dropdown', 'value'),
     Input('ent-dropdown', 'value'),
     Input('Fundamental-dd', 'value'),
     Input('Family-dd', 'value'),
     Input('EnterGradeTerm11', 'value'),
     Input('EnterGradeTerm21', 'value'),
     Input('EnterGradeTerm22', 'value'),
     Input('EnterGradeTerm31', 'value'),
     Input('EnterGradeTerm32', 'value'),
     Input('EnterGradeTerm41', 'value'),
     Input('EnterGradeTerm42', 'value'),
     Input('GPA_School', 'value'),]
)
def update_output(gen,maj,dep,sch,ent,fun,fam,t11,t12,t21,t22,t31,t32,t41,t42,gpa):
    you = {"MAJOR_NAME_THAI":maj,
           "DEPT_NAME_THAI":dep,
           "SEX_NAME_THAI":gen,
           "ENT_METHOD_DESC":ent,
           "PREV_INSTITUTION_NAME":sch,
           "เกรดปี1เทอม1":t11,
           "เกรดปี1เทอม2":t12,
           "เกรดปี2เทอม1":t21,
           "เกรดปี2เทอม2":t22,
           "เกรดปี3เทอม1":t31,
           "เกรดปี3เทอม2":t32,
           "เกรดปี4เทอม1":t41,
           "เกรดปี4เทอม2":t42,
           "GPA_SCHOOL":gpa,
           "FUND_NAME_CODE":fun,
           "PARENTS_MARRIED_NAME":fam}
    new_data = pd.DataFrame(data=you)
    return 


if __name__ == "__main__":
    app.run_server(debug=True)
