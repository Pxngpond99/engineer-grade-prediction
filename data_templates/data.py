import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

df= pd.read_excel('engineer-grade-prediction\data_analize\data_dropout_59-64.xlsx',usecols=['MAJOR_NAME_THAI','STUDY_STATUS',
    'เกรดปี1เทอม1', 'เกรดปี1เทอม2', 'เกรดปี1เทอม3',
    'เกรดปี2เทอม1', 'เกรดปี2เทอม2', 'เกรดปี2เทอม3',
    'เกรดปี3เทอม1', 'เกรดปี3เทอม2', 'เกรดปี3เทอม3',
    'เกรดปี4เทอม1', 'เกรดปี4เทอม2', 'เกรดปี4เทอม3', 
    'GPA_SCHOOL']).dropna() 
