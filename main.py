# Download the MP3 with yt-dlp 
# Download the instrumental + vocal

# The first query will be chosen and downloaded 
# The vocals and the instrumental will be layered 

# Slicing the sponsor block
# 


# importing packages
from pytube import YouTube
from pydub import AudioSegment
from os import path
import subprocess
import os
    

# Background Music 
def background_music():
    background_music = YouTube(str(input("Enter the URL of the background music of the song you wanna mix:")))
    print(background_music)
    video = background_music.streams.filter(only_audio=True).first()
    destination = "temp/"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = 'temp/'+'sound1' + '.mp3'
    os.rename(out_file, new_file)
    print(video.title + " has been successfully downloaded.")

# Vocals 
def vocals(): 
    vocals = YouTube(str(input("Enter the URL of the vocals of the song you wanna mix:")))
    print(vocals)
    video = vocals.streams.filter(only_audio=True).first()
    destination = "temp/"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = 'temp/' + 'sound2' + '.mp3'
    os.rename(out_file, new_file)
    print(vocals.title + " has been successfully downloaded.")

if input("Download Background Music(Y/N):") == "Y":
    background_music()
else: 
    exit()
if input("Download Vocals(Y/N):") == "Y":
    vocals()
else:
    exit()

if input("Do you want to mix both of the tracks? (Y/N):") == "Y":
    background_music = subprocess.call(['ffmpeg', '-i', 'temp/sound1.mp3',
                   'temp/sound1.wav'])
    vocals = subprocess.call(['ffmpeg', '-i', 'temp/sound2.mp3',
                   'temp/sound2.wav'])

    sound1 = AudioSegment.from_file("temp/sound1.wav")
    sound2 = AudioSegment.from_file("temp/sound2.wav")
    combined = sound1.overlay(sound2)
    combined.export("output.wav", format="wav")

else: 
    exit()


