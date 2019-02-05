# -*- coding: utf-8 -*-

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State# this import is for Dash callback functionality.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.externals import joblib
# import plotly.graph_objs as go
import pickle as pkl

# external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.config['suppress_callback_exceptions']=True


app = dash.Dash(__name__)
server = app.server # this is for deploying the app online.

app.layout = html.Div(children=[
    html.H1(children='Welcome to SleepAdvisor!',
        style={'marginTop':15,
        'textAlign':'center', 'color':'#2667B4', 'fontSize':'36', 'font-family':'Arial'}),
    html.H2(children='A web application meant to help you improve the quality of your sleep',
        style={'textAlign':'center', 'color':'#2667B4', 'font-family':'Arial'}),


    html.Div([
        html.Div(children=[
            html.Label('Please enter your age: '),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Age', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'color':'#2667B4', 'font-family':'Arial'}), style = {'padding':10}),



# dcc.RadioItems(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montréal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value='MTL'
# )


        html.Div(children=[
            html.Label('Please select your gender: '),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Dropdown(id='Gender',options=[
                {'label': 'Male', 'value': 1},
                {'label': 'Female', 'value': 0}
                ],
                ), style = {'marginLeft':20, 'width':'160', 'height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#3285E8', 'padding':10}),



        html.Div(children=[
            html.Label('Do you have high blood pressure? '),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Dropdown(id='BP',options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0},
                ],
                ), style = {'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#3285E8', 'padding':10}),



        html.Div(children=[
            html.Label('How many alcoholic drinks have you had in the past two weeks?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),

        html.Div(
            dcc.Input(id='AlcoholicDrinks', type='number', style = {
                'marginLeft':20, 'width':'160','height':'25',
                'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('How many 12-oz. caffeinated drinks (coffee, soda, tea) do you usually have in the morning?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Input(id='MorningCaffeine', type='number', style = {
                'marginLeft':20, 'width':'160','height':'25',
                'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('How many 12-oz. caffeinated drinks (coffee, soda, tea) do you usually have in the afternoon?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='AfternoonCaffeine', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('How many 12-oz. caffeinated drinks (coffee, soda, tea) do you usually have in the evening?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='EveningCaffeine', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10})],

        style={'display':'inline-block', 'width':'45%', 'vertical-align': 'top', 'horizontal-align':'center'}),



################# I want this to be a division between two columns on the webpage ##################



    html.Div([
        html.Div(children=[
            html.Label('Thinking about physical activities you do for at least 10 minutes at a time, which best describes your activity level?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Dropdown(id='ActivityLevel',options=[
                {'label': 'Litle to none', 'value': 1},
                {'label': 'Light', 'value': 2},
                {'label': 'Moderate', 'value': 3},
                {'label': 'Vigorous', 'value': 4},
                ],
                ), style = {'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4', 'padding':10}),



        html.Div(children=[
            html.Label('How much time per day (in hours) did you spend participating vigorous physical activities?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Vigorous', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('How much time per day (in hours) did you spend participating moderate-level physical activities?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Moderate', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('How much time per day (in hours) did you spend participating light physical activities?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Light', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('How much time (%) did you spend doing those activities indoors?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Indoors', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10}),



        html.Div(children=[
            html.Label('What is your BMI?'),
            ], style={'marginLeft':20, 'marginRight':20,
            'textAlign':'left', 'color':'#3285E8', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='BMI', type='number', style = {
            'marginLeft':20, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#2667B4'}), style ={'padding':10})],
        
        style={'display':'inline-block', 'width':'45%', 'vertical-align': 'top', 'horizontal-align': 'center'}),


    html.Div(
        html.Button('submit', id='age_button', style=
            {'float':'bottom', 'marginRight':30, 'color':'#4F1F90', 'fontSize':18, 'font-family':'Arial'})),

    html.Div(id='result', style = {'marginLeft':400, 'marginRight':400, 'width':'500','height':'30',
        'font-family':'Arial', 'fontSize':26,'color':'#2667B4', 'padding':20, 'horizontal-align':'center'})

    ])

@app.callback(
    Output('result', 'children'),
    [Input('age_button', 'n_clicks')],
    [State('Age', 'value'),
    State('Gender', 'value'),
    State('BP', 'value'),
    State('AlcoholicDrinks', 'value'),
    State('MorningCaffeine', 'value'),
    State('AfternoonCaffeine', 'value'),
    State('EveningCaffeine', 'value'),
    State('ActivityLevel', 'value'),
    State('Vigorous', 'value'),
    State('Moderate', 'value'),
    State('Light', 'value'),
    State('Indoors', 'value'),
    State('BMI', 'value')])

def predict_with_age(n_clicks, Age, Gender, BP, AlcoholicDrinks, MorningCaffeine, AfternoonCaffeine, EveningCaffeine,
    ActivityLevel, Vigorous, Moderate, Light, Indoors, BMI):

    Vars = [[Age, Gender, BP, AlcoholicDrinks, MorningCaffeine, AfternoonCaffeine, EveningCaffeine,
    ActivityLevel, Vigorous, Moderate, Light, Indoors, BMI]]
    result = model.predict(Vars)[0]
    return 'On a scale of 1 to 4 (4 being best), your sleep quality score is {:,.2f}.'.format(result, 1)

if __name__ == '__main__':
    model = joblib.load("./pickle_Random_Forest.pkl")
    app.run_server(debug=True)