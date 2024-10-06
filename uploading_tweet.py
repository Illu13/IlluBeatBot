import os
import urllib
from io import BytesIO
from time import sleep

from PIL import Image
import tweepy
from searching_song import get_song
from dotenv import load_dotenv

load_dotenv()
# Configura tus credenciales de Twitter
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
apiUploadTweet = tweepy.Client(consumer_key=API_KEY,
                               consumer_secret=API_SECRET_KEY,
                               access_token_secret=ACCESS_TOKEN_SECRET,
                               access_token=ACCESS_TOKEN,
                               bearer_token=BEARER_TOKEN)
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
    os.remove("song.png")

    return b
# Setup Tweepy API

auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY)
auth.set_access_token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
while True:
    song = get_song()
    photo = get_image(song[1])
    # Upload media to Twitter APIv1.1
    ret = api.media_upload(filename="proof", file=photo)
    apiUploadTweet.create_tweet(text=song[0], media_ids=[ret.media_id_string])
    print("Canción subida.")
    sleep(43200)


