from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Song:
    artist: str
    title: str
    mood: str
    tempo: str
    spotify_url: str


ARTISTS: List[str] = [
    "Tan Taşçı",
    "Ebru Gündeş",
    "Ebru Yaşar",
    "Tan Taşçı Başkanlar Korosu",
    "Sibel Can",
]


SONG_DB: List[Song] = [
    # Tan Taşçı - üzgün şarkılar (kullanıcının sağladığı linkler)
    Song(
        artist="Tan Taşçı",
        title="2mwkrqv...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/2mwkrqvumcoUE7v669QU4Q?si=d31029416278407a",
    ),
    Song(
        artist="Tan Taşçı",
        title="1UoOIt4...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/1UoOIt4oT3jLh4waq06wmG?si=ed269f388c2b42c5",
    ),
    Song(
        artist="Tan Taşçı",
        title="0bobhj6...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/0bobhj6j5Sonk9WVgTX0eS?si=4de5c421046047bd",
    ),
    Song(
        artist="Tan Taşçı",
        title="5becEVA...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/5becEVAzlXvCJRx5FN78YV?si=bfd9b11d1e1e474f",
    ),

    # Tan Taşçı - mutlu/enerjik şarkılar
    Song(
        artist="Tan Taşçı",
        title="1m8dcBT...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/1m8dcBTnQiIdk9voNq7en2?si=82817833e5514ccf",
    ),
    Song(
        artist="Tan Taşçı",
        title="0EeXAde...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/0EeXAdeYvbizvOIn0Ep7Q5?si=5055d34305a64d3b",
    ),
    Song(
        artist="Tan Taşçı",
        title="3UgdMot...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/3UgdMotqS12drlIRKCZ8kU?si=53c51f0f9f5d424b",
    ),

    # Tan Taşçı Başkanlar Korosu - mutlu
    Song(
        artist="Tan Taşçı Başkanlar Korosu",
        title="3ce8eEf...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/3ce8eEfOrfuHoZzWPxn8GV?si=e0625140f1dd4406",
    ),
    Song(
        artist="Tan Taşçı Başkanlar Korosu",
        title="7vL0pOi...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/7vL0pOilqmHCi58r2Keq49?si=b574fa0fc2124382",
    ),
    Song(
        artist="Tan Taşçı Başkanlar Korosu",
        title="artist-page",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/artist/3xlbBZQ5oyqwB1mTwCGeKV?si=98be93ab447b4f52",
    ),

    # Tan Taşçı Başkanlar Korosu - mutsuz
    Song(
        artist="Tan Taşçı Başkanlar Korosu",
        title="6YR8oK2...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/6YR8oK2vJENwqM0O874dKQ?si=1ead3a16ba2041d8",
    ),
    Song(
        artist="Tan Taşçı Başkanlar Korosu",
        title="0RzCciQ...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/0RzCciQT2gWgRZ73CmM8dV?si=c856bce09dfc4668",
    ),
    Song(
        artist="Tan Taşçı Başkanlar Korosu",
        title="4aOsWT8...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/4aOsWT8wFRdQu8YlCvKodO?si=b1e341c4a5ab49b4",
    ),

    # Sibel Can - üzgün
    Song(
        artist="Sibel Can",
        title="2MTKSYX...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/2MTKSYXPHasIPYt67pbCMI?si=8d9d1516c9be4e15",
    ),
    Song(
        artist="Sibel Can",
        title="6RKJ8nj...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/6RKJ8njrqpFn3FySuEMgRj?si=7b7ea7fc14dd4572",
    ),
    Song(
        artist="Sibel Can",
        title="67KwH1s...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/67KwH1swHlyFAvv9SEyqRh?si=4f7d2aceaa36454f",
    ),

    # Sibel Can - mutlu
    Song(
        artist="Sibel Can",
        title="1LLew0Q...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/1LLew0Q24EfhVRgHllvuf5?si=de5fb48f2cb246ed",
    ),
    Song(
        artist="Sibel Can",
        title="7859Rvo...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/7859Rvo6wXeImidBRL2dUZ?si=2b4ff637baa04b6a",
    ),

    # Ebru Gündeş - mutlu
    Song(
        artist="Ebru Gündeş",
        title="6JyMiVV...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/6JyMiVVXptfohf6S2zaAXv?si=d2859852c56c4008",
    ),
    Song(
        artist="Ebru Gündeş",
        title="4zTOUt...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/4zTOUtukd52LzS3bLWwzGc?si=57083aa761fb46be",
    ),
    Song(
        artist="Ebru Gündeş",
        title="4BkoGbx...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/4BkoGbx5pu2tlhFYymGgOi?si=9e173cc257514f25",
    ),
    Song(
        artist="Ebru Gündeş",
        title="3cmdwp2...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/3cmdwp2DrD7FnfW2wleT6M?si=65c02b1d1a5547d0",
    ),

    # Ebru Gündeş - mutsuz
    Song(
        artist="Ebru Gündeş",
        title="4wUW7kH...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/4wUW7kHHWkLQpcBbVAb6y6?si=17881e4922d84964",
    ),
    Song(
        artist="Ebru Gündeş",
        title="07ZQcQl...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/07ZQcQlbituG3sDXGKu4p3?si=044d59b1b4594d46",
    ),
    Song(
        artist="Ebru Gündeş",
        title="1U6b73M...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/1U6b73M2VWHTKiMu6IOzZr?si=6e26de4771674792",
    ),
    Song(
        artist="Ebru Gündeş",
        title="6IVIf0G...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/6IVIf0GA8vWOfskzTS5OUm?si=3a450bd49fc247f6",
    ),

    # Ebru Yaşar - mutlu / enerjik
    Song(
        artist="Ebru Yaşar",
        title="0cJiLWjG...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/0cJiLWjGfGZMGdhfcJv1ll?si=3a27ee6f6db643db",
    ),
    Song(
        artist="Ebru Yaşar",
        title="0Rb3Zf4w...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/0Rb3Zf4wemUX45NNoo5H0L?si=7e4a6117677145bc",
    ),
    Song(
        artist="Ebru Yaşar",
        title="0cqepWd8...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/0cqepWd80VJjK7JmzzN2IW?si=e58331ec664044ec",
    ),
    Song(
        artist="Ebru Yaşar",
        title="18aunlk8...",
        mood="mutlu",
        tempo="hizli",
        spotify_url="https://open.spotify.com/intl-tr/track/18aunlk8qbjM9yMlBEjeUs?si=fac2424166584e5b",
    ),

    # Ebru Yaşar - üzgün / sakin
    Song(
        artist="Ebru Yaşar",
        title="6wrijPgc...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/6wrijPgcUcXFBdpCOlHEfX?si=5e1dc39832204d7a",
    ),
    Song(
        artist="Ebru Yaşar",
        title="7fo4Scxp...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/7fo4ScxpiBnESWu8NRMyzx?si=03697f7f5b764f24",
    ),
    Song(
        artist="Ebru Yaşar",
        title="5f2EZOoz...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/5f2EZOoz3Zwf3A5e7zPigB?si=eeacadd1d3014090",
    ),
    Song(
        artist="Ebru Yaşar",
        title="26Ez7T2c...",
        mood="uzgun",
        tempo="slow",
        spotify_url="https://open.spotify.com/intl-tr/track/26Ez7T2cauSNRjHDFhigsT?si=eefafc0471a2485f",
    ),
]


