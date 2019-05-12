#!/usr/bin/env python3
# created by Jarrod Price
# the purpose of this script is to randomise a song from a directory that contains
# multiple audio files, and will play it via your default audio player

import os, webbrowser
from random import choice
from os.path import join, getsize, isdir

# this function will check if a given file is a supported format
def check_supported(filename):
    # if it is a directory skip it
    if isdir(file):
        return False
    supported = False
    audio_formats = ["mp3", "m4a", "wma", "aac", "flac", "wav"]
    for format in audio_formats:
        if file.endswith(f".{format}"):
            supported = True
            break
    return supported

# which directory to look for songs
songs_dir = "./songs"
# make sure the given path is a directory
if isdir(songs_dir):
    # create a list to keep track of our songs once they are found
    songs = []
    # perform a walk down the directory, this will fetch all files inside
    for root, dirs, files in os.walk(songs_dir):
        # loop through each file in this iteration of the walk
        for file in files:
            # check if the file is supported
            if not check_supported(file):
                continue
            else:
                # if we got till here add it to our list
                songs.append(join(root, file))
    # check if we got any results from the above operation
    if len(songs) > 0:
        # we should have songs to choose from
        # randomly choose an entry and open it in the default audio player
        webbrowser.open(choice(songs))
    else:
        print(f"'{songs_dir}' dir does not contain any supported song formats")
else:
    print(f"'{songs_dir}' dir is not found")
