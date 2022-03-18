import spotify_api as sapi
import pandas as pd

def getDataframeOfUser(user):
    #Creación del dataframe
    #dataframe = pd.DataFrame

    #Extraccion de las playlits de un usuario
    result_playlists = sapi.get_playlists_user(user)

    #Guardado de todos sus ids y nombres
    IDsPlaylists = []
    NamesPlaylists = []
    for playlist in result_playlists['items']:
        IDsPlaylists.append(playlist['id'])
        NamesPlaylists.append(playlist['name'])

    frames = []

    #Extraccion de todas las canciones de cada playlist
    for numId in range(0,len(IDsPlaylists)):
        df = getDataframeFromPlaylist(IDsPlaylists[numId])
        #Añadimos columna con el nombre de la playlist
        df['PlaylistName'] = NamesPlaylists[numId]
        frames.append(df)
        #dataframe = pd.concat(dataframe,df)

    return pd.concat(frames)

def getDataframeFromPlaylist(idPlaylist):
    #De cada playlist cogemos las canciones
    result_playlists_tracks = sapi.get_playlist_tracks(idPlaylist)
    tracks = result_playlists_tracks['items']
    #Lo convertimos a dataframe

    return pd.json_normalize(tracks)

    #Y almacenamos su artista y su nombre
    #artistas = result_playlists_tracks['items']['track']['artists'][0]

result = getDataframeOfUser('garciavicval')
result.to_csv('victorSongs.csv')
