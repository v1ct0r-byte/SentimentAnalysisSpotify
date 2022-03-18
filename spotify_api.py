import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config

client_credentials = SpotifyClientCredentials(client_id=config.spotify_key, client_secret=config.spotify_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)

def get_playlists_user(user):
    return(sp.user_playlists(user))

def get_playlist_tracks(playlist_id):
    return(sp.playlist_tracks(playlist_id))

def main():
    #results = get_playlists_user('markettes99')
    resultsVictor = get_playlists_user('garciavicval')
    result_playlist = get_playlist_tracks(resultsVictor['items'][0]['id'])
    for res in resultsVictor['items']:
        print(res['id'])

    for res in result_playlist['items']:
        print(res['track']['name'])


if __name__ == "__main__":
    main()
