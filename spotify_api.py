import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

import config

client_credentials = SpotifyClientCredentials(client_id=config.spotify_key, client_secret=config.spotify_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)

#Función que devuelve las playlists de un usuario
def get_playlists_user(user):
    return(sp.user_playlists(user))

#Función que devuelve las canciones de una playlist
def get_playlist_tracks(playlist_id):
    return(sp.playlist_tracks(playlist_id))

# Función que devuelve las features de una o varias canciones
# La entrada para el método tiene que ser un array de los IDs de las canciones
# El return devuelve un diccionario con el id de la canción como key junto con los valores de los distintos aspectos.
def get_audio_features(track_id):
    result = sp.audio_features(track_id)
    result = result[0]
    return result

def main():
    #result_playlists = get_playlists_user('markettes99')
    result_playlists = get_playlists_user('garciavicval')

    #IDs de las playlists extraídas
    for res in result_playlists['items']:
        print(res['id'])

    result_playlists_tracks = get_playlist_tracks(result_playlists['items'][0]['id'])

    #nombres y primer artista de las cancioens de la primera playlist
    # for res in result_playlists_tracks['items']:
    #     print(res['track']['name'] + ' -> ' + res['track']['artists'][0]['name'])

    # for res in result_playlists_tracks['items']:
    #     print(res)
    #     get_audio_features([res['track']['id']])

    #Radar chart for a song
    import spotify_api as sp
    import pandas as pd
    import plotly.express as px

    data,tempo = sp.get_audio_features('6rPO02ozF3bM7NnOV4h6s2')
    print(data)
    print(tempo)

    fig = px.line_polar(data, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    fig.show()




if __name__ == "__main__":
    main()
