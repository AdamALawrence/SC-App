import soundcloud
import requests
import time


r = requests.get('https://api.soundcloud.com/users/3207?client_id=7746f4238b8d4a91259513decb853667')

# create a client object with your app credentials
client = soundcloud.Client(client_id='7746f4238b8d4a91259513decb853667')

# a permalink to a track
track_url = 'http://soundcloud.com/forss/voca-nomen-tuum'

# resolve track URL into track resource
track = client.get('/resolve', url="https://soundcloud.com/musicis4lovers/jerome-price-repeat-myself-original-mix-musicis4loverscom")

# now that we have the track id, we can get a list of comments, for example
for track in client.get('/tracks/%d/comments' % track.id):
    print 'Someone said: %s at %d' % (comment.body, comment.timestamp)



