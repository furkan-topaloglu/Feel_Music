import webbrowser
from typing import Optional

from .data import Song


def format_song_info(song: Song) -> str:
    return (
        f"Sanatçı : {song.artist}\n"
        f"Şarkı   : {song.title}\n"
        f"Ruh hali: {song.mood} / Tempo: {song.tempo}\n"
        f"Spotify : {song.spotify_url}"
    )


def open_in_spotify(song: Song, *, open_in_browser: bool = True) -> Optional[bool]:
    if not open_in_browser:
        return None

    if not song.spotify_url:
        return False

    try:
        success = webbrowser.open(song.spotify_url)
        return bool(success)
    except Exception:
        return False



