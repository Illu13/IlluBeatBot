import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random




def get_song():
    SPOTIPY_CLIENT_ID = '0eecb56a6eb049d3929d302222b5304f'
    SPOTIPY_CLIENT_SECRET = '9c0409a3e6a24025ac883cc0e5862fba'

    # Configura la autenticación
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                               client_secret=SPOTIPY_CLIENT_SECRET))
    results = sp.playlist_items('5O01fBvvUwgr10tkVkx2wU')
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    selected_song_track = random.choice(tracks)['track']
    tweet_content = (f"Nombre: {selected_song_track['name']}\n"
                     f"Artista: {selected_song_track['artists'][0]['name']}\n"
                     f"Álbum: {selected_song_track['album']['name']}")
    photo = selected_song_track['album']['images'][0]['url']
    return [tweet_content, photo]
    # for item in tracks:
    #     track = item['track']
    #     print(f"Nombre: {track['name']}, Artista: {track['artists'][0]['name']}, Álbum: {track['album']['name']}")