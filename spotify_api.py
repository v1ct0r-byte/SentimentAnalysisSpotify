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
    get_playlists_user('markettes99')


if __name__ == "__main__":
    main()
