import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import seaborn as sns
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Input,Output, State

tsa = pd.read_csv("datatsa.csv")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app =dash.Dash(__name__,external_stylesheets=external_stylesheets)

def generate_table(dataframe,page_size=10):
    return dash_table.DataTable(
        id="dataTable",
        columns=[{
                "name":i,
                "id":i}
                for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action='native',
        page_current=0,
        page_size=page_size,
    )


app.layout =html.Div(children=[
    html.H1(children="Ujian Modul 2 Dashboard TSA"),

    dcc.Tabs(children =[
    dcc.Tab(value='tab1',label='Table Sample',children = [
        html.Div([
    
            html.Div([
                html.H1(children="DATAFRAME TSA"),
                #input writing (p = p)
                html.P('Claim Site'),
                #making a dropdown menu
                dcc.Dropdown(value='Yes',
                            id='filter-Claim Site',
                            options=[{'label':'Checkpoint', 'value': 'Checkpoint'},
                                    {'label':'Other','value':'Other'},
                                    {'label':'Checked Baggage','value':'Checked Baggage'},
                                    {'label':'Motor Vehicle','value':'Motor Vehicle'},
                                    {'label':'Bus Station','value':'Bus Station'}
                                    ])
        ]),
            html.Div([
                #input writing (p = p)
                html.P('Max Rows'),
                dcc.Input(
                    id='max-row',
                    placeholder='Enter a number...',
                    type='number',
                    value=10)
            ]),
            html.Br(),
            html.Button('Search',id = 'filter'),
            html.Br(),#break is an enter in between
            html.Div(id='div-table',children=[
                generate_table(tsa,page_size=10)]),
            html.Div([
            html.Div([
                html.Button('Previous')
            ],className='col-3'),
            html.Div([
                html.Button('Next',id='next')
            ],className='col-3')
            ])
                
    ],
    style = {
        'font-family': "Arial",
        'borderBottom': '1px solid #f2f2f2',
        'borderLeft': '1px solid #f2f2f2',
        'borderRight':'1px solid #f2f2f2',
        'padding' : '33px'}
    ),
    ]),

    dcc.Tab(value='tab3',label='Bar Chart',children =[
    #INPUTTING A TABLE TO THE TAB USING FUNCTION
        html.Div(children=[
            html.Div([
                #input writing (p = p)
                html.P('Y'),
                #making a dropdown menu
                dcc.Dropdown(value='Yes',
                            id='filer',
                            options=[{'label':'Claim Amount', 'value': 'Claim Amount'},
                                    {'label':'Close Amount','value':'Close Amount'},
                                    {'label':'Day Difference','value':'Day Difference'},
                                    {'label':'Amount Difference', 'value':'Amount Diff'}])
            ],
            className='col-3'),
            html.Div([
                #input writing (p = p)
                html.P('Y2'),
                #making a dropdown menu
                dcc.Dropdown(value='Yes',
                            id='filter-type',
                            options=[{'label':'Claim Amount', 'value': 'Claim Amount'},
                                    {'label':'Close Amount','value':'Close Amount'},
                                    {'label':'Day Difference','value':'Day Difference'},
                                    {'label':'Amount Difference', 'value':'Amount Diff'}])
            ],

            className='col-3'),
            html.Div([
                #input writing (p = p)
                html.P('X :'),
                #making a dropdown menu
                dcc.Dropdown(value='Sun',
                            id='type',
                            options=[{'label':'Claim Type', 'value': 'Claim Site'},
                                    {'label':'Claim Site','value':'Claim Site'},
                                    {'label':'Disposition','value':'Disposition'},
                                    ])
            ],className='col-3')

    ],className='row'),   


    dcc.Tab(value='tab2',label='SCatter-Chart',children = [
        dcc.Dropdown(value='Yes',
                            id='Pie-cHart',
                            options=[{'label':'Claim Amount', 'value': 'Claim Amount'},
                                    {'label':'Close Amount','value':'Close Amount'},
                                    {'label':'Day Difference','value':'Day Difference'},
                                    {'label':'Amount Difference', 'value':'Amount Diff'}]),
        html.Div([
            #MAKING NEW GRAPH
            dcc.Graph(
                id = 'graph-scatter',
                figure = {'data':[
                    go.Scatter(
                        x = tsa[tsa["Claim Type"]=='Property Damage']['Claim Amount'],
                        y = tsa[tsa["Claim Type"]=='Property Damage']['Close Amount'],
                        mode = 'markers',
                        name ='Proprety damage'),
                    go.Scatter(
                        x = tsa[tsa["Claim Type"]=='Passenger Property Loss']['Claim Amount'],
                        y = tsa[tsa["Claim Type"]=='Passenger Property Loss']['Close Amount'],
                        mode = 'markers',
                        name= 'Passenger Property Loss'),
                    go.Scatter(
                        x = tsa[tsa["Claim Type"]=='Passenger Theft']['Claim Amount'],
                        y = tsa[tsa["Claim Type"]=='Passenger Theft']['Close Amount'],
                        mode = 'markers',
                        name = 'Passenger Theft'),
                    go.Scatter(
                        x = tsa[tsa["Claim Type"]=='Employee Loss (MPCECA)']['Claim Amount'],
                        y = tsa[tsa["Claim Type"]=='Employee Loss (MPCECA)']['Close Amount'],
                        mode = 'markers',
                        name = ' Employee Lost'),
                    

            ],
            'layout': go.Layout(
                xaxis = {'title':'tip'},
                yaxis ={'title': 'Total Bill'},
                title = 'Tips Dash Scatter Visualization',
                hovermode = 'closest')
                })])
            ],
    # Style for the tabs
    style = {
        'font-family': "Arial",
        'borderBottom': '1px solid #f2f2f2',
        'borderLeft': '1px solid #f2f2f2',
        'borderRight':'1px solid #f2f2f2',
        'padding' : '33px'
    }),
    dcc.Tab(value='tab5',label='pie chart',children = [
        
    
        html.Div(children=[
        dcc.Graph(
        id='pie-chart',
        figure =
         {'data': [
            go.Pie(
            labels=['female','male'],
            values=[tsa[tsa['Claim Type']=='Property Damage']['Claim Amount'].mean(),
                    tsa[tsa['Claim Type']=='Passenger Property Loss']['Claim Amount'].mean(),
                    tsa[tsa['Claim Type']=='Employee Loss (MPCECA)']['Claim Amount'].mean(),
                    tsa[tsa['Claim Type']=='Passenger Theft']['Claim Amount'].mean()
                    ])],
            'layout': go.Layout(
            title = 'Tip mean divided by Sex')
          }
    )

    ])
])

])])

if __name__=='__main__':
    app.run_server(debug=True)