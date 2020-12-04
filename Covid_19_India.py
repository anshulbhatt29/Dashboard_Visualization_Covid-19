import pandas as pd
import plotly.express as px  # (version 4.7.0)


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app



df = pd.read_csv(r'C:\Users\anshu\Downloads\Covid_19_india.csv')
#print(df['Date'])
df['Date']=pd.to_datetime(df['Date'])
#print(df['Date'])
daf=df.loc[(df['Date']>='2020-02-01') & (df['Date']<='2020-02-29')]
da1=df.loc[(df['Date']>='2020-03-01') & (df['Date']<='2020-03-31')]
da2=df.loc[(df['Date']>='2020-04-01') & (df['Date']<='2020-04-30')]
da3=df.loc[(df['Date']>='2020-05-01') & (df['Date']<='2020-05-31')]
da4=df.loc[(df['Date']>='2020-06-01') & (df['Date']<='2020-06-30')]
da5=df.loc[(df['Date']>='2020-07-01') & (df['Date']<='2020-07-31')]
da6=df.loc[(df['Date']>='2020-08-01') & (df['Date']<='2020-08-30')]

#print(da2)
daf=daf.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()
da1=da1.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()
da2=da2.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()
da3=da3.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()
da4=da4.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()
da5=da5.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()
da6=da6.groupby(['State/UnionTerritory','Date'])[['Confirmed']].mean()




daf.reset_index(inplace=True)
da1.reset_index(inplace=True)
da2.reset_index(inplace=True)
da3.reset_index(inplace=True)
da4.reset_index(inplace=True)
da5.reset_index(inplace=True)
da6.reset_index(inplace=True)
#fig =px.bar(da3,x='State/UnionTerritory',y='Deaths')
#fig.show()

layout = html.Div([

    html.H1(" Dashboards For Covid-19 Cases In India", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "Feburary", "value":'Feburary'},
                     {"label": "March", "value":'March'},
                     {"label": "April", "value": 'April'},
                     {"label": "May", "value": 'May'},
                     {"label": "June", "value": 'June'},
                     {"label": "July", "value": 'July'},
                     {"label": "August", "value":'August'}],
                 multi=False,
                 value='Feburary',
            
                 
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):


    
    container = "The year chosen by user was: {}".format(option_slctd)
    if option_slctd=='Feburary' :
         dff=daf
    if option_slctd=='March' :
         dff=da1
    elif option_slctd=='April':
         dff=da2
    elif option_slctd=='May':
         dff=da3
    elif option_slctd=='June':
         dff=da4  
    elif option_slctd=='July':
         dff=da5
    elif option_slctd=='August':
         dff=da6 


    fig =px.bar(dff,x='State/UnionTerritory',y='Confirmed')
    return container, fig
    
     
    

    