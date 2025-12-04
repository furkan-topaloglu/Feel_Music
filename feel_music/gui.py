import ttkbootstrap as tb
from tkinter import messagebox

from .data import SONG_DB
from .mood_engine import pick_random_song
from .player import format_song_info, open_in_spotify


class FeelMusicApp(tb.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Feel Music – Ruh Halinle Çal")
        self.geometry("760x480")
        self.resizable(False, False)

        self.text_primary = "#E6EEF8"
        self.text_secondary = "#B6C7E6"
        self.muted = "#9FB0D1"

        self.current_song = None
        self._build_ui()

    def _build_ui(self):
        card = tb.Frame(self, bootstyle="secondary", padding=(16, 12))
        card.place(relx=0.5, rely=0.5, anchor="center", width=700, height=420)

        title = tb.Label(
            card,
            text="Bugün ruh halin nasıl?",
            font=("Segoe UI", 20, "bold"),
            bootstyle="secondary",
            foreground=self.text_primary,
        )
        title.pack(pady=(0, 6))

        subtitle = tb.Label(
            card,
            text="Bir ruh hali seç: sana uygun bir şarkı açayım.",
            font=("Segoe UI", 11),
            bootstyle="secondary",
            foreground=self.text_secondary,
        )
        subtitle.pack(pady=(0, 8))

        btn_frame = tb.Frame(card, bootstyle="secondary")
        btn_frame.pack(pady=(0, 8))

        def make_button(text, style, cmd):
            return tb.Button(btn_frame, text=text, bootstyle=style, width=20, padding=8, command=cmd)

        btn_mutlu = make_button("Mutlu / Enerjik", "success", lambda: self._on_mood_selected("mutlu"))
        btn_huzun = make_button("Hüzünlü / Sakin", "info", lambda: self._on_mood_selected("uzgun"))
        btn_surpriz = make_button("Sürpriz 🎲", "warning", lambda: self._on_mood_selected("surpriz"))

        btn_mutlu.grid(row=0, column=0, padx=8, pady=6)
        btn_huzun.grid(row=0, column=1, padx=8, pady=6)
        btn_surpriz.grid(row=1, column=0, columnspan=2, pady=8)

        result_frame = tb.Frame(card, bootstyle="secondary")
        result_frame.pack(fill="both", expand=True, padx=6, pady=(6, 0))

        result_title = tb.Label(
            result_frame,
            text="Seçilen şarkı",
            bootstyle="secondary",
            font=("Segoe UI", 10, "bold"),
            foreground=self.muted,
        )
        result_title.pack(anchor="w")

        self.result_label = tb.Label(
            result_frame,
            text="Henüz bir şarkı seçilmedi.",
            bootstyle="secondary",
            anchor="nw",
            justify="left",
            font=("Consolas", 11),
            wraplength=640,
            foreground=self.text_primary,
        )
        self.result_label.pack(fill="both", expand=True, pady=(6, 6))

    def _on_mood_selected(self, mood):
        mood_key = "bilinmiyor" if mood == "surpriz" else mood
        song = pick_random_song(SONG_DB, mood_key)
        info = format_song_info(song)

        self.current_song = song
        self.result_label.config(text=info)

        ok = open_in_spotify(song, open_in_browser=True)
        if ok is False:
            messagebox.showwarning("Spotify açılamadı", "Tarayıcı açılamadı. Manuel açabilirsin.")


def run_gui():
    app = FeelMusicApp()
    app.mainloop()


if __name__ == "__main__":
    run_gui()
