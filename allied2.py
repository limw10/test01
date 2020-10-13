import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#E8EAED',
    'text': '#7FDBFF'
}

df1 = pd.read_csv("./200920_Evaluation Data.csv")
df1[['ID','REF_NO']] = df1[['ID','REF_NO']].astype('str')

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children='Allied Group Evaluation Dashboard', style={"textAlign": "center"}),

    html.Div(children='''
        Welcome to Allied Group Data Science interactive dashboard.
    ''', style={"textAlign": "center"}),

    dcc.Tabs(id='tabs', children=[
      dcc.Tab(label='Tab 1', children = [

    html.H1(children='Analytics 1', style={"textAlign": "center"}),

    dcc.Dropdown(id='my-dropdown',
    			options=[{'label': 'Penang', 'value': 'PENANG'},
    				     {'label': 'Kuala Lumpur', 'value': 'KUALA LUMPUR'}],
    		    multi=True,value=['PENANG'],
                style={"display": "block", "margin-left": "auto", 
                        "margin-right": "auto", "width": "60%"}),

    dcc.Graph(
        id='example-graph',
        style={'height': 600,
               'width': 900,
               "display": "block",
               "margin-left": "auto",
               "margin-right": "auto"}
        #figure=fig
        ),
    html.H1(children='Analytics 2', style={"textAlign": "center"}),

    dcc.Dropdown(id='my-dropdown2',
          options=[{'label': 'Penang', 'value': 'PENANG'},
                 {'label': 'Kuala Lumpur', 'value': 'KUALA LUMPUR'}],
            multi=True,value=['PENANG'],
                style={"display": "block", "margin-left": "auto", 
                        "margin-right": "auto", "width": "60%"}),

    dcc.Graph(
        id='example-graph2',
        style={'height': 600,
               'width': 900,
               "display": "block",
               "margin-left": "auto",
               "margin-right": "auto"}
        #figure=fig
        )
], className='container'),

    dcc.Tab(label='Tab 2', children = [

    html.H1(children='Analytics 3', style={"textAlign": "center"}),

    dcc.Dropdown(id='my-dropdown3',
          options=[{'label': 'Penang', 'value': 'PENANG'},
                 {'label': 'Kuala Lumpur', 'value': 'KUALA LUMPUR'}],
            multi=True,value=['PENANG'],
                style={"display": "block", "margin-left": "auto", 
                        "margin-right": "auto", "width": "60%"}),

    dcc.Graph(
        id='example-graph3',
        style={'height': 600,
               'width': 900,
               "display": "block",
               "margin-left": "auto",
               "margin-right": "auto"}
        #figure=fig
        ),
    html.H1(children='Analytics 4', style={"textAlign": "center"}),

    dcc.Dropdown(id='my-dropdown4',
          options=[{'label': 'Penang', 'value': 'PENANG'},
                 {'label': 'Kuala Lumpur', 'value': 'KUALA LUMPUR'}],
            multi=True,value=['PENANG'],
                style={"display": "block", "margin-left": "auto", 
                        "margin-right": "auto", "width": "60%"}),

    dcc.Graph(
        id='example-graph4',
        style={'height': 600,
               'width': 900,
               "display": "block",
               "margin-left": "auto",
               "margin-right": "auto"}
        #figure=fig
        )
])

])

])

@app.callback(Output('example-graph','figure'),
			 [Input('my-dropdown', 'value')])

def update_figure(selected_state):

    dropdown = {"PENANG": "Penang", "KUALA LUMPUR": "Kuala Lumpur"}
    trace1 = []
    for state in selected_state:
        trace1.append(
            go.Scatter(x=df1[df1["STATE"] == state]["TOTAL_REVENUE"],
                       y=df1[df1["STATE"] == state]["STAFF_COSTS_ACCOUNTS"],
                       mode='markers',opacity=0.7, text=df1['PROJECT_NAME'], marker_size=8,
                       name=f'{dropdown[state]}',textposition='bottom right')) 
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(#colorway=["#EF963B", "#FF0056"],
               height=600,
               width=950,
               #hovermode='closest',
               title = 'Total Revenue vs Account Cost',
               #style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'},
               xaxis={"title": "Total Revenue"},
               yaxis={"title": "Total Accounts Cost"},
               paper_bgcolor = colors['background'],
               plot_bgcolor = colors['background'],
               #margin=dict(l=20, r=20, t=20, b=20,pad=4),
               autosize = True)}
    return figure

@app.callback(Output('example-graph2','figure'),
       [Input('my-dropdown2', 'value')])

def update_figure(selected_state):

    dropdown = {"PENANG": "Penang", "KUALA LUMPUR": "Kuala Lumpur"}
    trace1 = []
    for state in selected_state:
        trace1.append(
            go.Scatter(x=df1[df1["STATE"] == state]["MANAGEMENT_FEES"],
                       y=df1[df1["STATE"] == state]["STAFF_COSTS_ACCOUNTS"],
                       mode='markers',opacity=0.7, text=df1['PROJECT_NAME'], marker_size=8,
                       name=f'{dropdown[state]}',textposition='bottom right')) 
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(#colorway=["#EF963B", "#FF0056"],
               height=600,
               width=950,
               #hovermode='closest',
               title = 'Management Fees vs Account Cost',
              # style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'},
               xaxis={"title": "Management Fees"},
               yaxis={"title": "Total Accounts Cost"},
               paper_bgcolor = colors['background'],
               plot_bgcolor = colors['background'],
               #margin=dict(l=20, r=20, t=20, b=20,pad=4),
               autosize = False)}
    return figure

@app.callback(Output('example-graph3','figure'),
       [Input('my-dropdown3', 'value')])

def update_figure(selected_state):

    dropdown = {"PENANG": "Penang", "KUALA LUMPUR": "Kuala Lumpur"}
    trace1 = []
    for state in selected_state:
        trace1.append(
            go.Bar(x=df1[df1["STATE"] == state]["YEAR"],
                       y=df1[df1["STATE"] == state]["STAFF_COSTS_ACCOUNTS"],
                       #mode='markers',opacity=0.7, text=df1['PROJECT_NAME'], marker_size=8,
                       name=f'{dropdown[state]}'))#,textposition='bottom right')) 
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(#colorway=["#EF963B", "#FF0056"],
               height=600,
               width=950,
               #hovermode='closest',
               title = 'Total Account Cost',
              # style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'},
               xaxis={"title": "Year"},
               yaxis={"title": "Total Accounts Cost"},
               paper_bgcolor = colors['background'],
               plot_bgcolor = colors['background'],
               #margin=dict(l=20, r=20, t=20, b=20,pad=4),
               autosize = True)}
    return figure

@app.callback(Output('example-graph4','figure'),
       [Input('my-dropdown4', 'value')])

def update_figure(selected_state):

    dropdown = {"PENANG": "Penang", "KUALA LUMPUR": "Kuala Lumpur"}
    trace1 = []
    for state in selected_state:
        trace1.append(
            go.Scatter(x=df1[df1["STATE"] == state]["MANAGEMENT_FEES"],
                       y=df1[df1["STATE"] == state]["STAFF_COSTS_ACCOUNTS"],
                       mode='markers',opacity=0.7, text=df1['PROJECT_NAME'], marker_size=8,
                       name=f'{dropdown[state]}',textposition='bottom right')) 
    traces = [trace1]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(#colorway=["#EF963B", "#FF0056"],
               height=600,
               width=950,
               #hovermode='closest',
               title = 'Management Fees vs Account Cost',
              # style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'},
               xaxis={"title": "Management Fees"},
               yaxis={"title": "Total Accounts Cost"},
               paper_bgcolor = colors['background'],
               plot_bgcolor = colors['background'],
               #margin=dict(l=20, r=20, t=20, b=20,pad=4),
               autosize = True)}
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)