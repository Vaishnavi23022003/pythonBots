from bs4 import BeautifulSoup
import requests, spotipy, webbrowser
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = "ef2a4acc75d44036bab9a38b7f97a64f"
SPOTIFY_SECRET = "9292e47369ee48959249905666c1231d"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
# print(user_id)

url = "https://www.billboard.com/charts/hot-100/"

print("Which date do you want to travel to ?")
year = input("Year (YYYY) : ")
month = input("Month (MM) : ")
day = input("Day (DD) : ")

url += year + "-" + month + "-" + day

res = requests.get(url=url)

soup = BeautifulSoup(res.text, "html.parser")

songList=soup.find_all(name="span",class_="chart-element__information__song text--truncate color--primary")

song_uri=[]

for song in songList:
    result = sp.search(q="track:"+song.text+" year:"+year, type="track")
    try:
        song_uri.append(result["tracks"]["items"][0]["uri"])
    except:
        print("Failed: ",song.text)


playList=sp.user_playlist_create(f"{user_id}", f"{year}/{month}/{day} Billboard 100", public=False, collaborative=False, description='')
playList_id=playList["id"]
playList_link=playList["external_urls"]["spotify"]
print("Link to playlist:",playList_link)

sp.user_playlist_add_tracks(f"{user_id}", f"{playList_id}", song_uri, position=None) #depricated 😑
# sp.playlist_add_items(f"{playList_id}", song_uri, position=None)

webbrowser.open(playList_link)