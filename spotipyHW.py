import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import json

credentials = oauth2.SpotifyClientCredentials(client_id='26b486e6ddb841d190834b7dce27c20a', client_secret='f57c30c5d2e44d8385a384b85c04a687')
token = credentials.get_access_token()
token = util.prompt_for_user_token(
        username='gleekyninja22',
        scope='user-top-read',
        client_id='26b486e6ddb841d190834b7dce27c20a',
        client_secret='f57c30c5d2e44d8385a384b85c04a687',
        redirect_uri='http://google.com')
spotify = spotipy.Spotify(auth=token)

#artist uri
top_uri = 'spotify:artist:5RADpgYLOuS2ZxDq7ggYYH'
#get albums
results = spotify.artist_albums(top_uri, album_type='album')
albums = results['items']
albs =[]
for album in albums:
    albs.append(album['id'])
tr = []
for a in albs:
    #get tracks
    t = spotify.album_tracks(a)
    tracks = t['items']
    for track in tracks:
        name = track['name']
        if "-" not in name and name not in tr:
            #get name
            tr.append(name)
            i = track['id']
            #get features
            features = spotify.audio_features([i])
            print(name)
            print(features)
            '''
            for ind in range(len(features)):
                print(feature_names[ind] + " " + str(features[ind]))
                print('')
            '''
h