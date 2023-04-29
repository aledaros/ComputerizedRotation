import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred
from datetime import datetime


scope = "user-library-read playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.CLIENT_ID, client_secret= cred.CLIENT_SECRET, redirect_uri=cred.REDIRECT_URI, scope=scope))

savedTracks = sp.current_user_saved_tracks(limit=50)
arrToAdd = []
for idx, item in enumerate(savedTracks['items']):
    track = item['track']
    arrToAdd.append(track['uri'])

playlistTracks = sp.playlist_items('INSERT_PLAYLIST_URI')
arr = []
for idx, item in enumerate(playlistTracks['items']):
    playlistTrack = item['track']
    arr.append(playlistTrack['uri'])

sp.playlist_remove_all_occurrences_of_items('INSERT_PLAYLIST_URI', arr)
sp.playlist_add_items('INSERT_PLAYLIST_URI', arrToAdd)