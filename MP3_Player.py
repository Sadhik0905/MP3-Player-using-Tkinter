# Importing Modules
import pygame
import tkinter as tk 
from tkinter.filedialog import askdirectory
import os

# Creating Application Window
musicplayer = tk.Tk()

# Giving Title to the Application
musicplayer.title("MUSIC PLAYER")

# Setting Dimensions to the window
musicplayer.geometry("450x350")

# Asking for Music Directory
directory = askdirectory()

# Setting Music Directory to the current working directory
os.chdir(directory)

# Creating Songlist
# os.listdir() returns the list containing the names of entries in the directory given by the path
songlist = os.listdir()
# print(songlist)
# Creating the playlist
playlist = tk.Listbox(musicplayer,font="cambria 14 bold",bg="cyan2",selectmode=tk.SINGLE)

# Adding songs from songlist to the playlist

pos = 0
for i in songlist:
    playlist.insert(pos,i)
    pos = pos+1


# Initializing modules
pygame.init() 
pygame.mixer.init()

# Function for PLAY button
def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()


# Function for STOP button
def ExitMusicPlayer():
    pygame.mixer.music.stop()


# Function for PAUSE button
def Pause():
    pygame.mixer.music.pause()


# Function for RESUME button
def Resume():
    pygame.mixer.music.unpause()



# Button For Play
Button_Play = tk.Button(musicplayer,width=5,height=3,text="Play Music",font="cambria 14 bold",command=play,bg="lime green",fg="black")
Button_Stop = tk.Button(musicplayer,width=5,height=3,text="Stop Music",font="cambria 14 bold",command=ExitMusicPlayer,bg="red",fg="black")
Button_Pause = tk.Button(musicplayer,width=5,height=3,text="Pause Music",font="cambria 14 bold",command=Pause,bg="yellow",fg="black")
Button_Resume = tk.Button(musicplayer,width=5,height=3,text="Resume Music",font="cambria 14 bold",command=Resume,bg="lime green",fg="black")

Button_Play.pack(fill="x")
Button_Stop.pack(fill="x")
Button_Pause.pack(fill="x")
Button_Resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tk.StringVar()
songtitle = tk.Label(musicplayer,font="cambria 14 bold",textvariable=var)
songtitle.pack()


musicplayer.mainloop()
