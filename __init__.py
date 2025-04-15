from dotenv import load_dotenv
import os
from download_manager import DownloadManager

SPOTIFY_ID = os.getenv("SPOTIFY_ID_KEY")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET_KEY")
GENIUS_TOKEN = os.getenv("GENIUS_TOKEN_KEY")
PLAYLIST_LINK = "https://open.spotify.com/playlist/6GDqHRPPt8e4IbCx5zebDw?si=eb785862ce08419e"
PLAYLIST_LINK_2 = "https://open.spotify.com/playlist/0B0pah8vd5GVUsuMZm1fOv?si=00aa0e5956984bf8"
pla ="https://open.spotify.com/playlist/37i9dQZF1DWZUozJiHy44Y?si=LJNropBqTciLZQ4yWerbnQ"
AlBUM_LINK = "https://open.spotify.com/album/21jF5jlMtzo94wbxmJ18aa?si=vIQQrK3ySZK4kuTHUGKsTA"

my_downloaded = DownloadManager(SPOTIFY_ID, SPOTIFY_SECRET, GENIUS_TOKEN,  directory ="./Desktop/Songs")

my_downloaded.start_downloader(PLAYLIST_LINK)