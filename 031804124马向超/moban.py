import random
import os
import pygame
import time
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

class yd:
    flag=0
    place=''
    dire=''
    def choose(self, BPM):
        if BPM<100:
            self.flag=1
        elif 100 < BPM < 150:
            self.flag=2
        elif BPM >150:
            self.flag=3

    def judge(self,place):
        if self.flag==1:
            dire='流行'
            self.place= os.path.join(place,dire)
        if self.flag==2:
            dire='电音'
            self.place= os.path.join(place,dire)
        if self.flag==3:
            dire='激昂'
            self.place= os.path.join(place,dire)
    def select(self):
        filenum = 0
        self.mp3=[]
        for lists in os.listdir(self.place):
            sub_path = os.path.join(self.place, lists)
            self.mp3.append(sub_path)
            if os.path.isfile(sub_path):
                filenum = filenum + 1
        self.num=random.randint(1,filenum)
        print(self.mp3[self.num])

    def doit(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.mp3[self.num])
        pygame.mixer.music.play(start=0.0)
        time.sleep(300)
        pygame.mixer.music.stop()

    def start(self,BPM,place):
        self.choose(BPM)
        self.judge(place)
        self.select()
        self.doit()


BPM=input("输入BPM:")
BPM=int(BPM)
place='F:\My Special Image\音乐'
yundong=yd()
yundong.start(BPM,place)