import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config

client_credentials = SpotifyClientCredentials(client_id=config.spotify_key, client_secret=config.spotify_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)

#Función que devuelve las playlists de un usuario
def get_playlists_user(user):
    return(sp.user_playlists(user))

#Función que devuelve las canciones de una playlist
def get_playlist_tracks(playlist_id):
    return(sp.playlist_tracks(playlist_id))

def main():
    #result_playlists = get_playlists_user('markettes99')
    result_playlists = get_playlists_user('garciavicval')

    #IDs de las playlists extraídas
    for res in result_playlists['items']:
        print(res['id'])

    result_playlists_tracks = get_playlist_tracks(result_playlists['items'][0]['id'])

    #nombres y primer artista de las cancioens de la primera playlist
    for res in result_playlists_tracks['items']:
        print(res['track']['name'] + ' -> ' + res['track']['artists'][0]['name'])

    for res in result_playlists_tracks['items']:
        print(res)


if __name__ == "__main__":
    main()
