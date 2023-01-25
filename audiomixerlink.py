
from tkinter import * 
from pydub import AudioSegment
from pytube import YouTube
import subprocess
import os
import json
from os import path
import tkinter.messagebox
from youtube_search import YoutubeSearch
import webbrowser

w = Tk()

w.title("Audio Mixer")
w.config(bg="#282828")
w.resizable(height=False, width=False)
def open_html():
    filename = 'file:///'+os.getcwd()+'/' + 'index.html'
    webbrowser.open_new_tab(filename)


def download_background_music():
    y=background_music_entry.get()
    background_music = YouTube(y)
    video = background_music.streams.filter(only_audio=True).first()
    destination = "temp/"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = 'temp/'+'sound1' + '.mp3'
    os.rename(out_file, new_file)
    tkinter.messagebox.showinfo("Information", "Your background music has been downloaded") 
    background_music_download.configure(state=DISABLED)

def download_vocal():
    x=vocals_entry.get()
    vocals = YouTube(x)
    video = vocals.streams.filter(only_audio=True).first()
    destination = "temp/"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = 'temp/'+'sound2' + '.mp3'
    os.rename(out_file, new_file)
    tkinter.messagebox.showinfo("Information",  "Your vocals has been downloaded")
    vocals_download.configure(state=DISABLED)

def overlay_button():
    background_music_download.configure(state=NORMAL)
    vocals_download.configure(state=NORMAL)
    background_music = subprocess.call(['ffmpeg', '-i', 'temp/sound1.mp3',
                   'temp/sound1.wav'])
    vocals = subprocess.call(['ffmpeg', '-i', 'temp/sound2.mp3',
                   'temp/sound2.wav'])

    sound1 = AudioSegment.from_file("temp/sound1.wav")
    sound2 = AudioSegment.from_file("temp/sound2.wav")
    combined = sound1.overlay(sound2)
    combined.export("output.wav", format="wav")
    tkinter.messagebox.showinfo("Information", "Your tracks have been overlayed, Your file has been saved to output.wav")    
    play_overlayed_song = Button(w, text="Play overlayed song", font=fonts, command=open_html)
    play_overlayed_song.grid(row=4, column=1, padx=10, pady=10)
    os.system("sudo rm temp/*")

"""
    path = "temp/"
    for file_name in os.listdir(path):
        # construct full file path
        file = path + file_name
        if os.path.isfile(file):
            print('Deleting file:', file)
            os.remove(file)
"""
fonts = ("Cascadia Code", "18")


title_label = Label(w, text="Audio Mixer", font=fonts, fg="white", bg="#282828")
title_label.grid(row=0, column=1, padx=10, pady=10)

background_music_label = Label(w, text="Enter Background Music \nLink(Youtube): ", font=fonts, fg="white", bg="#282828")
background_music_label.grid(row=1, column=0, padx=10, pady=10)

background_music_entry = Entry(w, font=fonts, width=25)
background_music_entry.grid(row=1, column=1, padx=10, pady=10)

# Background Music button 
background_music_download = Button(w, text="Download Background track", font=fonts, command=download_background_music)
background_music_download.grid(row=1, column=2, padx=10, pady=10)

vocals_label = Label(w, text="Enter Vocals \nLink(Youtube): ", font=fonts, fg="white", bg="#282828")
vocals_label.grid(row=2, column=0, padx=10, pady=10)

vocals_entry = Entry(w, font=fonts, width=25)
vocals_entry.grid(row=2, column=1, padx=10, pady=10)

# Download vocal button 
vocals_download = Button(w, text="Download vocal track", font=fonts, command=download_vocal)
vocals_download.grid(row=2, column=2, padx=10, pady=10)


overlay_process_button = Button(w, text="Start", font=fonts, command=overlay_button)
overlay_process_button.grid(row=3, column=1, padx=10, pady=10)

w.mainloop()
