import random
from typing import Iterable, List

from .data import Song


MOOD_MAPPING = {
    "mutlu": "mutlu",
    "iyi": "mutlu",
    "harika": "mutlu",
    "süper": "mutlu",
    "enerjik": "mutlu",
    "enerji": "mutlu",
    "uzgun": "uzgun",
    "üzgün": "uzgun",
    "mutsuz": "uzgun",
    "kırgın": "uzgun",
    "yalnız": "uzgun",
    "düşük": "uzgun",
    "kötü": "uzgun",
    "sakin": "sakin",
    "yorgun": "sakin",
    "dingin": "sakin",
    "huzurlu": "sakin",
}


def normalize_mood(raw_mood: str) -> str:
    key = raw_mood.strip().lower()
    return MOOD_MAPPING.get(key, key)


def filter_songs_by_mood(songs: Iterable[Song], mood: str) -> List[Song]:
    if mood == "mutlu":
        allowed_moods = ["mutlu", "enerjik"]
    elif mood == "enerjik":
        allowed_moods = ["enerjik", "mutlu"]
    elif mood == "uzgun":
        allowed_moods = ["uzgun", "sakin"]
    elif mood == "sakin":
        allowed_moods = ["sakin", "uzgun"]
    else:
        allowed_moods = ["mutlu", "enerjik", "uzgun", "sakin"]

    return [song for song in songs if song.mood in allowed_moods]


def pick_random_song(songs: Iterable[Song], mood: str) -> Song:
    candidates = filter_songs_by_mood(list(songs), mood)
    if not candidates:
        candidates = list(songs)
    return random.choice(candidates)



