from click import option
from dash import *
import plotly.express as px
import pandas as pd
import playlistsProcessing as pp
import emotions as em

user_df = pd.DataFrame()
playlists = []
songsList = []

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
        dcc.Slider(id='slider',min=1,value=1,step=1,max=2),
        html.Button(id='analize',children='Analizar',n_clicks=0),
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
    global user_df
    user_df = pd.DataFrame()
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
    Output('slider','max'),
    Input('playlist','value'),
)
def get_songs(value):
    global user_df, songsList
    songs_df = user_df[user_df['PlaylistName']==value]
    songsList = []
    for index, row in songs_df.iterrows():
        songsList.append({'artist':row['ArtistName'],'song':row['SongName']})
    
    return len(songsList)
    
    
@app.callback(
    Output('sentiment-graph','figure'),
    Input('analize', 'n_clicks'),
    State('slider','value')
)
def show_graph(nclicks, value):
    global songsList,user_df
    songsList = songsList[0:value]
    print(songsList)
    res_df = em.getLyricsInfo(songsList)
    #merged_df = user_df.merge(res_df,'left',left_on='SongName',right_on='title')
    res_df.to_csv('carlos2.csv',index='false')
    #merged_df.to_csv('carlos3.csv',index='false')
    max_range = max(res_df['positive'].max(),res_df['negative'].max())
    max_range *= 1.05
    fig = px.scatter(res_df,'positive', 'negative',range_x=[-0.01,max_range], range_y=[-0.01,max_range],symbol='artist',color="title")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)