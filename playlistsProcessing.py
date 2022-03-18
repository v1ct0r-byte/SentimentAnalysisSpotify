import spotify_api as sapi
import pandas as pd

#Extraccion de las playlits de un usuario
result_playlists = sapi.get_playlists_user('garciavicval')
#Guardado de todos sus ids y nombres
IDsPlaylists = []
NamesPlaylists = []
for playlist in result_playlists['items']:
    IDsPlaylists.append(playlist['id'])
    NamesPlaylists.append(playlist['name'])


#Creación del dataframe
dataframe = pd.Dataframe()

#Extraccion de todas las canciones de cada playlist
for id in IDsPlaylists:
    #De cada playlist cogemos las canciones
    result_playlists_tracks = sapi.get_playlist_tracks(id)
    #Y almacenamos su artista y su nombre