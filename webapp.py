from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Analizador de sentimientos'),

    html.Div(children='''
        Analiza los sentimientos que transmiten la música que escuchas en Spotify
    '''),
    html.Br(),
    html.Div(children=[
        html.Label(children='Introduce tu usuario '),
        dcc.Input(
            id="inputuser",
            type='text',
            placeholder="usuario",
        ),
    ]),html.Br(),
    html.Div(children=[
        html.Label(children='Selecciona una playlist '),
        dcc.Dropdown(, 'NYC', id='demo-dropdown'),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)