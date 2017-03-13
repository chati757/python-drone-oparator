#!/usr/bin/env python
#-*-coding: utf-8 -*-
from unicurses import *
#
NEW_COLOR_NUM=1

def new_color(fg,bg):
    global NEW_COLOR_NUM

    color_number = NEW_COLOR_NUM
    init_pair(color_number,fg,bg)
    NEW_COLOR_NUM +=1
    
    return color_number