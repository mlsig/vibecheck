import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import json

#this method from spotipy docs
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print(str(i) + " " + track['artists'][0]['name'] + " " + track['name'])
#end method
        
credentials = oauth2.SpotifyClientCredentials(client_id='26b486e6ddb841d190834b7dce27c20a', client_secret='f57c30c5d2e44d8385a384b85c04a687')
token = credentials.get_access_token()
token = util.prompt_for_user_token(
        username='gleekyninja22',
        scope='user-top-read',
        client_id='26b486e6ddb841d190834b7dce27c20a',
        client_secret='f57c30c5d2e44d8385a384b85c04a687',
        redirect_uri='http://google.com')
spotify = spotipy.Spotify(auth=token)

#get playlist (dict)
playlist = spotify.user_playlist('gleekyninja22', playlist_id='37i9dQZF1EtlFPUefKa7S5', fields="tracks,next");
#get the tracks (dict)
tracks = playlist['tracks']
show_tracks(tracks)
while tracks['next']:
    tracks = spotipy.next(tracks)
    show_tracks(tracks)    
'''
#scrape all songs, calc averages
checking = True
while(checking):     
    #song to "vibe check"
    track_uri = ''
    #scrape stats on song
    i = track['id']
    features = spotify.audio_features([i])
    #compare with the averages
    #predict like or no like
    #have user confirm
    #update personal stats by using song to update averages if it predicts like
    #prompt user to exit or go again
'''    
