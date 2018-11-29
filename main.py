# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x=1
import pygame as pg

pg.init()
bgColor = (46,150,61)
scrW = 800
scrH = 600

screen = pg.display.set_mode((scrW,scrH),0,24)
screen.fill(bgColor)

while True:
    pg.event.get()
    pg.display.update()
    










