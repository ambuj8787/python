# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:29:04 2023

@author: user
"""

from pytube import YouTube
link=r'https://www.youtube.com/watch?v=jkx0xj41uz4='
yt=YouTube(link)
mp4files=yt.Filter('mp4')
yt.set_filename('video')

d_video=yt.get(mp4files[-1].extension, mp4files[-1].resolution)

d_video.download(r"C:\Users\user")