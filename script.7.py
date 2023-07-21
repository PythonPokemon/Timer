import tkinter as tk
import time
import pygame
from tkinter import filedialog
import shutil
import os

selected_music = "Tyga.mp3"  # Standard-Klingelton
music_folder = "music_db"  # Zielordner für die Musikdatenbank

# Überprüfen und Erstellen des Musikordners, falls er nicht existiert
if not os.path.exists(music_folder):
    os.makedirs(music_folder)

# Pygame initialisieren (nur einmal aufrufen)
pygame.mixer.init()

def start_timer():
    global remaining_time
    remaining_time = int(entry.get())
    update_timer()

def stop_timer():
    global remaining_time
    remaining_time = 0
    label.config(text="Timer gestoppt!")
    pygame.mixer.music.stop()

def update_timer():
    global remaining_time
    if remaining_time > 0:
        label.config(text=f"Verbleibende Zeit: {remaining_time} Sekunden")
        remaining_time -= 1
        root.after(1000, update_timer)  # Aktualisierung alle 1000 Millisekunden (1 Sekunde)
    else:
        label.config(text="Zeit abgelaufen!")
        play_music()

def play_music():
    pygame.mixer.music.load(selected_music)
    pygame.mixer.music.play()

def browse_music():
    global selected_music
    selected_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if selected_file:
        selected_music = selected_file
        update_selected_music_label()

def update_selected_music_label():
    selected_music_label.config(text=f"Ausgewählter Klingelton: {selected_music}")

def add_music():
    global selected_music
    selected_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if selected_file:
        selected_music = selected_file
        filename = os.path.basename(selected_music)
        destination = os.path.join(os.path.dirname(__file__), music_folder, filename)
        shutil.copy(selected_music, destination)
        update_selected_music_label()

root = tk.Tk()
root.title("Timer")

label = tk.Label(root, text="Timer einstellen (in Sekunden):")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_timer)
stop_button.pack()

browse_button = tk.Button(root, text="Durchsuchen", command=browse_music)
browse_button.pack()

add_music_button = tk.Button(root, text="Neue Musik hinzufügen", command=add_music)
add_music_button.pack()

selected_music_label = tk.Label(root, text=f"Ausgewählter Klingelton: {selected_music}")
selected_music_label.pack()

root.mainloop()
