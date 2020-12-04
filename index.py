
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app

# Connect to your app pages
#from apps import vgames, global_sales
import Covid_19_India
import Covid_19_World

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Covid_19_Cases_India', href='/Covid/India'),
        dcc.Link('Covid_19_Cases_Worldwide', href='/Covid/World'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Covid/India':
        return Covid_19_India.layout
    if pathname == '/Covid/World':
        return Covid_19_World.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)