import spotipy

#export SPOTIPY_CLIENT_ID = '136c655a58a24f98a4bb9142c6925bd1'
#export SPOTIPY_CLIENT_SECRET = '60ac28c38b36430ebb06ab53e1ba7cf9'

from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None