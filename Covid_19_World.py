import pandas as pd
import plotly.express as px  # (version 4.7.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
from dash.exceptions import PreventUpdate
from app import app

#external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#gf=pd.read_csv(r'C:\Users\anshu\Desktop\covid_19_clean_complete.csv')
gf=pd.read_csv(r'C:\Users\anshu\Downloads\full_data.csv')
#list=gf['Country/Region']
list=gf['location']
import pycountry
countries={}
for country in pycountry.countries:
    countries[country.name]=country.alpha_3
codes=[countries.get(country,'Unknown code') for country in list]
#print(codes)
gf['iso_alpha']=codes



#gf['Date']=pd.to_datetime(gf['Date'])
gf['date']=pd.to_datetime(gf['date'])
#print(df['Date'])
ga1=gf.loc[(gf['date']>='2020-01-01') & (gf['date']<='2020-01-31')]
ga2=gf.loc[(gf['date']>='2020-02-01') & (gf['date']<='2020-02-29')]
ga3=gf.loc[(gf['date']>='2020-03-01') & (gf['date']<='2020-03-31')]
ga4=gf.loc[(gf['date']>='2020-04-01') & (gf['date']<='2020-04-30')]
ga5=gf.loc[(gf['date']>='2020-05-01') & (gf['date']<='2020-05-31')]
ga6=gf.loc[(gf['date']>='2020-06-01') & (gf['date']<='2020-06-30')]
ga7=gf.loc[(gf['date']>='2020-07-01') & (gf['date']<='2020-07-31')]
ga8=gf.loc[(gf['date']>='2020-08-01') & (gf['date']<='2020-08-31')]
ga9=gf.loc[(gf['date']>='2020-09-01') & (gf['date']<='2020-09-30')]
ga10=gf.loc[(gf['date']>='2020-10-01') & (gf['date']<='2020-10-14')]

"""

ga1=ga1.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
ga2=ga2.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
ga3=ga3.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
ga4=ga4.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
ga5=ga5.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
ga6=ga6.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
ga7=ga7.groupby(['Country/Region','iso_alpha','Date'])[['Confirmed']].mean()
"""
ga1=ga1.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga2=ga2.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga3=ga3.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga4=ga4.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga5=ga5.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga6=ga6.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga7=ga7.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga8=ga8.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga9=ga9.groupby(['location','iso_alpha'])[['total_cases']].mean()
ga10=ga10.groupby(['location','iso_alpha'])[['total_cases']].mean()


ga1.reset_index(inplace=True)
ga2.reset_index(inplace=True)
ga3.reset_index(inplace=True)
ga4.reset_index(inplace=True)
ga5.reset_index(inplace=True)
ga6.reset_index(inplace=True)
ga7.reset_index(inplace=True)
ga8.reset_index(inplace=True)
ga9.reset_index(inplace=True)
ga10.reset_index(inplace=True)


layout = html.Div([

    html.Div([
        dcc.Graph(id='the_graph')
    ]),
      dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "January", "value":'January'},
                     {"label": "Feburary", "value":'Feburary'},
                     {"label": "March", "value":'March'},
                     {"label": "April", "value": 'April'},
                     {"label": "May", "value": 'May'},
                     {"label": "June", "value": 'June'},
                     {"label": "July", "value": 'July'},
                     {"label": "August", "value": 'August'},
                     {"label": "September", "value": 'September'},
                     {"label": "October", "value": 'October'}],
                 multi=False,
                 value='January',
            
                 
                 style={'width': "40%"}
                 ),

    html.Div([
        html.Button(id='submit_button', n_clicks=0, children='Submit'),
        html.Div(id='output_state'),
    ],style={'text-align': 'center'}),

])

#---------------------------------------------------------------

@app.callback(
    [Output('output_state', 'children'),
    Output(component_id='the_graph', component_property='figure')],
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='slct_year', component_property='value')]
)

def update_output(num_clicks, option_slctd):
    if option_slctd is None:
        raise PreventUpdate 
    elif option_slctd=='January' :
        dff=ga1
    elif option_slctd=='Feburary' :
         dff=ga2
    if option_slctd=='March' :
         dff=ga3
    elif option_slctd=='April':
         dff=ga4
    elif option_slctd=='May':
         dff=ga5
    elif option_slctd=='June':
         dff=ga6  
    elif option_slctd=='July':
         dff=ga7
    elif option_slctd=='August':
         dff=ga8
    elif option_slctd=='September':
         dff=ga9
    elif option_slctd=='October':
         dff=ga10

    fig=px.choropleth(dff,locations="iso_alpha",
                  color="total_cases",
                  hover_name="location",
                  projection='natural earth',
                  title='Covid_19_cases_Worldwide',
                  color_continuous_scale=px.colors.sequential.Plasma)

    fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                          margin=dict(l=60, r=60, t=50, b=50))

    return ('The input value was "{}" and the button has been \
                clicked {} times'.format(option_slctd, num_clicks), fig)


"""
fig=px.choropleth(ga6,locations="iso_alpha",
                  color="Confirmed",
                  hover_name="Country/Region",
                  projection='natural earth',
                  title='fuck',
                  color_continuous_scale=px.colors.sequential.Plasma)
fig.show()
"""

