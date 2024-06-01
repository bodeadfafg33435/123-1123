from tkinter import *
import time
import random
import pygame

class Ball():

        def__init__(self, canvas, platform, color):
        self.canvas = canvas
        self.platform = platform
        self.onval = canvas.creatr_oval(200, 200, 215, 215 fill=color)
        self.dir = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.dir)
        self.y = -1
        self.touch_bottom = False

    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3]  >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 400:
            self.touch_bottam = True
        if self.touch_platfom(pos) ==  True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 500:
            self.x = -3

class Platform():
    def__init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)

