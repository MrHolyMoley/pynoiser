from tkinter import *
from tkinter import ttk
import pygame

brown_noise = "brown-noise.mp3"

# Create window.
window = Tk()
window.title = "Pynoiser"
window.geometry("400x400")
window.configure(background = "gray27")
#frame = ttk.Frame(window, padding = 10)

# Title Text
title_label = Label(window, text = "Pynoiser", font = "Monospace 24", foreground = "white", background = "gray27")
title_label.pack(pady = 10)

info_label = ttk.Label(window, text = "A simple brown noise player", font = "Monospace 16", foreground = "white", background = "gray27")
info_label.pack(pady = 10)

footer_label = ttk.Label(window, text = "github.com/TheJoelFelton", font = "Monospace 10", foreground = "white", background = "gray27")
footer_label.pack(side = "bottom", pady = 10)

# Initiate the Pygame Audio mixer
pygame.mixer.init()

# Play sounds
def play():
    pygame.mixer.music.load(brown_noise)
    pygame.mixer.music.play(loops = 10)

def stop():
    pygame.mixer.music.stop()

# Buttons for window
play_btn = ttk.Button(window, text = "Play", command = play)
play_btn.pack(pady = 20)

stop_btn = ttk.Button(window, text = "Stop", command = stop)
stop_btn.pack(pady = 10)

quit_btn = ttk.Button(window, text = "Quit", command = window.destroy)
quit_btn.pack(side = "bottom", pady = 15)

# Keep Window open
window.mainloop()