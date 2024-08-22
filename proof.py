import urllib

import tweepy
from io import BytesIO
from PIL import Image
import tweepy
from spotipy_proof import get_song

# Configura tus credenciales de Twitter
API_KEY = 'nrJPIDLN0nDQ6ll0vhaEYZnTa'
API_SECRET_KEY = 'CfqRJkGvOXqIKkdJsK2uryXv5jA8tER2ac0VTQiLlF7cHrAhtX'
ACCESS_TOKEN = '1292156552-BGnNixXUIjg8FiE4NxPpqBdZWijzdLTE2syTxKY'
ACCESS_TOKEN_SECRET = 'go6zriYLyPyxxveS32zVKo1P7vywm0gS5NSgHGCz91qhJ'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
apiUploadTweet = tweepy.Client(consumer_key=API_KEY,
                               consumer_secret=API_SECRET_KEY,
                               access_token_secret=ACCESS_TOKEN_SECRET,
                               access_token=ACCESS_TOKEN,
                               bearer_token='AAAAAAAAAAAAAAAAAAAAAP34vQEAAAAAr1a6lhs0FnSVXQiy7Rx97QTXlQs%3Djz45zLDyV9KWM8kKS2zhfRX53AcBHFEejuTF7HmDMzgGQWnb1m')


# Example image manipulation

def get_image(photo):
    img_link = urllib.request.urlretrieve(
        photo,
        "song.png")
    img = Image.open("song.png")
    # Do something to the image...

    # Save image in-memory
    b = BytesIO()
    img.save(b, "PNG")
    b.seek(0)
    return b


# Setup Tweepy API
auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY)
auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
song = get_song()
photo = get_image(song[1])
# Upload media to Twitter APIv1.1
ret = api.media_upload(filename="proof", file=photo)
apiUploadTweet.create_tweet(text=song[0], media_ids=[ret.media_id_string])
