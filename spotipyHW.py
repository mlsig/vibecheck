import spotipy
import spotipy.oauth2 as oauth2
import spotipy.util as util
import json

def avg_valnc(tracks,psize):
    valnc = 0
    for i, item in enumerate(tracks['items']):
        track = item['track']
        t = track['id']
        feats = spotify.audio_features([t])
        valnc = valnc + float(feats[0]['valence'])
    return valnc / psize
        
credentials = oauth2.SpotifyClientCredentials(client_id='26b486e6ddb841d190834b7dce27c20a', client_secret='f57c30c5d2e44d8385a384b85c04a687')
token = credentials.get_access_token()
token = util.prompt_for_user_token(
        username='gleekyninja22',
        scope='user-top-read',
        client_id='26b486e6ddb841d190834b7dce27c20a',
        client_secret='f57c30c5d2e44d8385a384b85c04a687',
        redirect_uri='http://google.com')
spotify = spotipy.Spotify(auth=token)

#get playlist (dict) smash bros and chill -> .7
playlist = spotify.user_playlist('gleekyninja22', playlist_id='4rWMkQBEqtw86orhlqB7bP', fields="tracks,next");
pSize = 420
#get the tracks (dict)
tracks = playlist['tracks']
#scrape all songs
print("Analyzing initial data...")
avgV = avg_valnc(tracks,pSize)
#print(str(avgV))
print("Completed initial Vibechecks.")
#do the things
checking = True
while(checking):
    #song to "vibe check"
    track_uri = input("What song should I vibecheck? Input track URI: ")
    #scrape stats on song
    track = spotify.track(track_uri)
    name = i = track['name']
    i = track['id']
    features = spotify.audio_features([i])
    currV = float(features[0]['valence'])
    #print(str(currV))
    #calc percent diff with average
    percentDiff = (abs(avgV-currV) / ((avgV+currV)/2)) * 100
    #print(str(percentDiff))
    if(percentDiff < 15):
        print("This song should match the vibe of the playlist")
    else:
        print("This song might not match the vibe of the playlist")
    Vcheck = input("What's your take? Enter 'yes' if it matches and 'no' if it doesn't: ")
    if(Vcheck == "yes"):
        temp = avgV * pSize
        pSize = pSize + 1
        avgV = (temp + currV) / pSize
    status = input("Enter 'done' or 'continue': ")
    if(status == "done"):
        print("Thanks for checking your vibes with me :3")
        checking = False
                  
