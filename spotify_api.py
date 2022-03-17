import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config


client_credentials = SpotifyClientCredentials(client_id=config.spotify_key, client_secret=config.spotify_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)

def get_playlists_user(user):
    results = sp.user_playlists(user)
    print(results)

def main():
    get_playlists_user('markettes99')


if __name__ == "__main__":
    main()
