from dash import *
import plotly.express as px
import pandas as pd
from spotify_api import *

playlists = []

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
            placeholder="Escribe aquí el usuario",
        ),
    ]),
    html.Br(),
    html.Div(id='sel-playlist',children=[
        html.Label(children='Selecciona una playlist '),
        dcc.Dropdown(id='playlist'),
    ]),
    html.Div(id='sel-playlist',children=[
        html.Label(children='Selecciona una playlist '),
        dcc.Dropdown(id='playlist'),
    ]),
])

@app.callback(
    Output('playlist','options'),
    Input('inputuser','value'),
)
def get_playlist(value):
    #lo que está haciendo victor
    results = get_playlists_user(value)
    df = pd.DataFrame()
    for item in results['items']:
        tracknames = item['name']
        ids = item['id']
    df['name'] = tracknames
    df['id'] = ids
    print(df.head())
    playlists = {}
    for 
    playlists = {'label':results['items'][0]['name'],'value':results['items'][0]['id']} #0 no, todas

    return [playlists]

@app.callback(
    Output('playlist','options'),
    Input('playlist','value'),
)
def get_songs():
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)