import json
import requests
from librespot.core import Session
from librespot.audio.decoders import AudioQuality
from bot.helpers.translations import lang

class SpotifyAPI:
    def __init__(self):
        self.session = None
        self.token = None
        self.quality = AudioQuality.HIGH
        self.music_format = "ogg"
        self.reencode = False

    async def login(self, user_name, password):
        """Login to Spotify."""
        # Use environment variables or a more secure method for credentials
        self.session = Session.Builder().user_pass(user_name, password).create()

    async def get_song_info(self, song_id):
        """Get information about a Spotify song."""
        try:
            url = f"https://api.spotify.com/v1/tracks?ids={song_id}&market=from_token"
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            info = response.json()["tracks"][0]
            is_playable = info["is_playable"]
            if not is_playable:
                return None, lang.select.ERR_SPOT_NOT_AVAIL
            return info, None
        except requests.RequestException as e:
            # Log the exception or raise a specific exception for better debugging
            pass
    
    def handle_quality(self, data=None):
        'Sets quality if input given else returns cuurent quality'
        if data == 160: self.quality = AudioQuality.HIGH
        elif data == 320: self.quality = AudioQuality.VERY_HIGH
        else:
            if spotify.quality == AudioQuality.HIGH:
                return 160
            else: return 320
# Instantiate the SpotifyAPI class
spotify = SpotifyAPI()
