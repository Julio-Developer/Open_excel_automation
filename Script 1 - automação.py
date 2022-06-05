# -*- coding: utf-8 -*-
from turtle import position
import pyautogui as pg

# Getting the mouse positon
pg.sleep(4)
print(pg.position())

# Clicking on a defined position
pg.moveTo(x=670, y=1051)