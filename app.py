# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event # this import is for Dash callback functionality.
from sklearn.externals import joblib
import plotly.graph_objs as go
import pickle as pkl

# external_stylesheets = ["https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app.config['suppress_callback_exceptions']=True

app = dash.Dash(__name__)
server = app.server # this is for deploying the app online.

model = pkl.load(open("pickle_Random_Forest_Week4.pkl", 'rb'))
# document.body.style.backgroundColor = "red"

colors = {
    'background': '#E3E9EE'
    }

# Add a background color to style 'backgroundColor' - pick color from HTML color picker.
app.layout = html.Div(style = {'backgroundColor':colors['background'], 'horizontal-align':'center'}, children=[
    html.H1(children='Welcome to SleepAdvisor!',
        style={'paddingTop':50,
        'textAlign':'center', 'color':'#618FAE', 'fontSize':'36', 'font-family':'Arial'}),
    html.H2(children='A web application meant to help you improve the quality of your sleep',
        style={'textAlign':'center', 'color':'#859CAB', 'font-family':'Arial', 'marginBottom':50}),


    html.Div([
        html.Div(children=[
            html.Label('Please enter your age: '),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Age', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'color':'#667E8D', 'font-family':'Arial'}, value = 30), style = {'padding':10}),



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
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Dropdown(id='Gender',options=[
                {'label': 'Male', 'value': 1},
                {'label': 'Female', 'value': 0}
                ], value = 1
                ), style = {'marginLeft':60, 'width':'160', 'height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D', 'padding':10}),



        html.Div(children=[
            html.Label('Do you have high blood pressure? '),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Dropdown(id='BP',options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0},
                ], value = 0
                ), style = {'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D', 'padding':10}),



        html.Div(children=[
            html.Label('How many alcoholic drinks have you had in the past two weeks?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),

        html.Div(
            dcc.Input(id='AlcoholicDrinks', type='number', style = {
                'marginLeft':60, 'width':'160','height':'25',
                'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 6), style ={'padding':10}),



        html.Div(children=[
            html.Label('How many 12-oz. caffeinated drinks (coffee, soda, tea) do you usually have in the morning?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Input(id='MorningCaffeine', type='number', style = {
                'marginLeft':60, 'width':'160','height':'25',
                'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 3), style ={'padding':10}),



        html.Div(children=[
            html.Label('How many 12-oz. caffeinated drinks (coffee, soda, tea) do you usually have in the afternoon?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='AfternoonCaffeine', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 2), style ={'padding':10}),



        html.Div(children=[
            html.Label('How many 12-oz. caffeinated drinks (coffee, soda, tea) do you usually have in the evening?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='EveningCaffeine', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 1), style ={'padding':10})],

        style={'display':'inline-block', 'width':'45%', 'vertical-align':'top', 'horizontal-align':'center'}),



################# I want this to be a division between two columns on the webpage ##################



    html.Div([
        html.Div(children=[
            html.Label('Thinking about physical activities you do for at least 10 minutes at a time, which best describes your activity level?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(
            dcc.Dropdown(id='ActivityLevel',options=[
                {'label': 'Litle to none', 'value': 1},
                {'label': 'Light', 'value': 2},
                {'label': 'Moderate', 'value': 3},
                {'label': 'Vigorous', 'value': 4},
                ], value = 1
                ), style = {'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D', 'padding':10}),



        html.Div(children=[
            html.Label('How much time per day (in hours) did you spend participating vigorous physical activities?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Vigorous', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 0), style ={'padding':10}),



        html.Div(children=[
            html.Label('How much time per day (in hours) did you spend participating moderate-level physical activities?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Moderate', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 0), style ={'padding':10}),



        html.Div(children=[
            html.Label('How much time per day (in hours) did you spend participating light physical activities?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Light', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 0), style ={'padding':10}),



        html.Div(children=[
            html.Label('How much time (%) did you spend doing those activities indoors?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='Indoors', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 50), style ={'padding':10}),



        html.Div(children=[
            html.Label('What is your BMI?'),
            ], style={'marginLeft':60, 'marginRight':20,
            'textAlign':'left', 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'}),
        html.Div(dcc.Input(id='BMI', type='number', style = {
            'marginLeft':60, 'width':'160','height':'25',
            'fontSize':16, 'font-family':'Arial', 'color':'#667E8D'}, value = 28), style ={'padding':10}),



        html.Div(
        	html.Button('submit', id='age_button', style=
        		{'marginRight':0, 'color':'#667E8D', 'fontSize':18, 'font-family':'Arial'
        		}), style = {'paddingLeft':60})],

        	style={'display':'inline-block', 'width':'45%', 'vertical-align': 'top', 'horizontal-align':'center'}),


    # html.Div(
    # 	html.Button('submit', id='age_button', style=
    # 		{'float':'bottom', 'marginRight':30, 'color':'#4F1F90', 'fontSize':18, 'font-family':'Arial',
    # 		'horizontal-align':'center'})),

    html.Div(id='result', style = {'marginLeft':200, 'marginRight':200, 'width':'1000','height':'30',
    	'font-family':'Arial', 'fontSize':26,'color':'#859CAB', 'paddingTop':50, 'paddingBottom':25,
    	'horizontal-align':'center'}),


    dcc.Graph(
    	id='Graph', style = {'height': 500, 'width':1000, 'marginLeft':200, 'marginRight':200},
    	figure={
    	'data': [],
    	# 'marker':{'color':'#859CAB'},
    	'layout': {
    	'plot_bgcolor': colors['background'],
    	'paper_bgcolor': colors['background']
    	}
    	}
    	)
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

@app.callback(
	Output('Graph', 'figure'),
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
	return {
	'data': [
	{'x': ['sleep scores'], 'y': [2.67], 'type':'bar', 'name':'Population Average Sleep Quality Score'},
	{'x': ['sleep scores'], 'y': [result], 'type':'bar', 'name':'Your Sleep Quality Score'},
	{'x': ['sleep scores'], 'y': [4], 'type':'bar', 'name':'Your Sleep Quality Score Following Top Recommendation'}],
	# 'marker':{'bar_bcolor':colors['rgb(204,204,204)','rgb(222,45,38)', 'rgb(222,45,38)']},
	'layout':{
    	'plot_bgcolor': colors['background'],
    	'paper_bgcolor': colors['background']
    	}
    }

if __name__ == '__main__':
#    model = joblib.load("./pickle_Random_Forest.pkl")
    app.run_server(debug=True)