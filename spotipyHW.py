import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import json

def track_feat(tracks):
    allFeats = []
    for i, item in enumerate(tracks['items']):
        track = item['track']
        t = track['id']
        feats = spotify.audio_features([t])
        allFeats.append(feats)
    return allFeats
        
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
#scrape all songs
print("Scraping initial data...")
songFeatures = track_feat(tracks)
#calc averages
print("Analyzing data...")


#do the things
print("Completed initial Vibechecks.")
checking = True
while(checking):
    #song to "vibe check"
    track_uri = input("What song should I vibecheck? Input track URI: ")
    #scrape stats on song
    track = spotify.track(track_uri)
    name = i = track['name']
    i = track['id']
    features = spotify.audio_features([i])
    print(name)
    print(features)
    #compare with the averages
    #predict like or no like
    #have user confirm
    #update personal stats by using song to update averages if it predicts like
    status = input("Enter 'done' or 'continue': ")
    if(status == "done"):
        print("Thanks for checkign your vibes with me :3")
        checking = False
                  
