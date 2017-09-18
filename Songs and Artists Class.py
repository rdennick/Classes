#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Getting artists and song titles
class Artist:
    def __init__(self,name,label):
        self.name = name
        self.label = label
        
class Song:
    def __init__(self,name,album,year,artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist

artist = Artist("Taylor Swift","Big Machine Records, LLC")
song_1 = Song("You Belong With Me","Fearless",2008,artist)
song_2 = Song("All Too Well","Red",2012,artist)
artist2 = Artist("LIGHTS","Warner Bros. Records Inc.")
song_3 = Song("Up We Go","Midnight Machines",2016,artist2)


def get_song_title(obj):
    return '"'+obj.name+'"'+" - "+obj.artist.name + "("+str(obj.year)+")"
    
print(get_song_title(song_3))
