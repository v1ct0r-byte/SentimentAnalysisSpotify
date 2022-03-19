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
    #for numId in range(0,len(IDsPlaylists)): #Creo que yo tengo muchas voy a poner solo las 5 primeras
    for numId in range(0,min(len(IDsPlaylists),20)):
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

    #Recopilación por orden del artista principal de cada composición musical
    artists = []
    for track in tracks:
        artists.append(track['track']['artists'][0]['name'])

    #Lo convertimos a dataframe
    trackDataframe = pd.json_normalize(tracks)

    #Renombramos columnas
    columnsDataFrame = trackDataframe.columns
    #Renombramos columnas
    trackDataframe.rename(columns={columnsDataFrame[5]:'UserOwner',columnsDataFrame[15]:'AlbumName',columnsDataFrame[16]:'SongReleaseDate',columnsDataFrame[21]:'ArtistName',columnsDataFrame[26]:'SongIsExplicit',columnsDataFrame[32]:'SongName'},inplace=True)
    
    #Dejamos solo las columans que nos interesan
    trackDataframe = trackDataframe[['UserOwner','AlbumName','SongReleaseDate','ArtistName','SongIsExplicit','SongName']]

    #Sustituimos la columna de artistas por el artista principal de la canción
    trackDataframe['ArtistName'] = artists

    return trackDataframe

#Descomentar para ver un csv con los datos extraídos
#result = getDataframeOfUser('garciavicval')
#result.to_csv('victorSongs.csv')
