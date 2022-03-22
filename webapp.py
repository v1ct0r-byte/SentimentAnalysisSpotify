from click import option
from dash import *
import plotly.express as px
import pandas as pd
import processing as pp
import emotions as em

user_df = pd.DataFrame()
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
        html.Button(id='buscar',children='Buscar',n_clicks=0)
    ]),
    html.Br(),
    html.Div(id='sel-playlist',children=[
        html.Label(children='Selecciona una playlist '),
        dcc.Dropdown(id='playlist'),
    ]),
    html.Br(),
    html.Div(children=[
        html.Label(children='Gráfica de sentimiento de la playlist seleccionada'),
        dcc.Graph(id='sentiment-graph'),
    ]),
])

@app.callback(
    Output('playlist','options'),
    Input('buscar', 'n_clicks'),
    State('inputuser','value'),
)
def get_playlists(clicks,value):
    #lo que está haciendo victor
    global user_df
    user_df = pp.getDataframeOfUser(value)
    res = user_df['PlaylistName'].unique()
        

    #results = get_playlists_user(value)
    # df = pd.DataFrame()
    # for item in user_df['PlaylistName']:
    #     tracknames = item['name']
    #     ids = item['id']
    # df['name'] = tracknames
    # df['id'] = ids
    # print(df.head())
    # playlists = {}
    # playlists = {'label':results['items'][0]['name'],'value':results['items'][0]['id']} #0 no, todas

    return res

@app.callback(
    Output('sentiment-graph','figure'),
    Input('playlist','value'),
)
def get_songs(value):
    global user_df
    songs_df = user_df[user_df['PlaylistName']==value]
    songsList = []
    for index, row in songs_df.iterrows():
        songsList.append({'artist':row['ArtistName'],'song':row['SongName']})
    print(songsList)
    songsList = songsList[0:4]
    res_df = em.getLyricsInfo(songsList)
    max_range = max(res_df['positive'].max(),res_df['negative'].max())
    max_range *= 1.05
    fig = px.scatter(res_df,'positive', 'negative',range_x=[-0.01,max_range], range_y=[-0.01,max_range],symbol='artist',color="title")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)